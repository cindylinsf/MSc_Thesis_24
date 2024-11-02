import requests
from bs4 import BeautifulSoup
import json
import csv
from config import load_config
from login_bank2 import login
import os
import time
import random
from log_utils import setup_anonymized_logging

# Configure Logging
logger = setup_anonymized_logging()

def get_profile_links(session, page_number):
    """
    Extract profile links from a page.
    
    Args:
        session: requests.Session object
        page_number: Current page number to scrape
    """
    try:
        # Construct page URL using the pattern from config
        page_url = f"{bank_config['base_url']}{bank_config['search_url_pattern'].format(page=page_number)}"
        
        response = session.get(page_url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        
        profile_links = []
        links = soup.find_all('a', href=True)
        for link in links:
            href = link['href']
            if '/catalogue/products/donor-' in href:
                # Clean up the URL - remove any domain if present
                clean_href = href.replace(bank_config['base_url'], '')
                # Ensure it starts with a forward slash
                if not clean_href.startswith('/'):
                    clean_href = '/' + clean_href
                profile_links.append(clean_href)
        
        logger.info(f"Found {len(profile_links)} profile links on page {page_number}")
        for link in profile_links:
            logger.debug(f"Found profile link: {link}")
            
        time.sleep(random.uniform(1, 3))
        return profile_links
        
    except Exception as e:
        logger.error(f"Error getting profile links from page {page_number}: {str(e)}")
        return []

def scrape_profile(relative_url):
    """
    Scrape a single profile from the given URL.
    """
    try:
        full_url = f"{bank_config['base_url']}{relative_url}"
        response = session.get(full_url)
        response.raise_for_status()
        
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            
            if any([
                soup.find('div', class_='profile'),
                soup.find('h1', class_='profile__name'),
                soup.find('div', class_='profile__intro')
            ]):
                # Extract donor ID
                donor_id_elem = soup.find('h1', class_='cell-12 profile__name') or soup.find('h1', class_='profile__name')
                donor_id = donor_id_elem.text.strip() if donor_id_elem else "Not found"
                
                # Extract donor description
                description_div = soup.find('div', class_='cell small-12 profile__intro')
                donor_description = "Not found"
                donor_quote = "Not found"
                
                if description_div:
                    paragraphs = description_div.find_all('p')
                    description_parts = []
                    
                    for p in paragraphs:
                        text = ''.join(p.strings)
                        if '\"' in text:
                            donor_quote = text.strip()
                        else:
                            description_parts.append(text.strip())
                    
                    donor_description = ' '.join(description_parts)

                # Extract interests and hobbies
                interests_and_hobbies = "Not found"
                skills = "Not found"
                
                detail_wrappers = soup.find_all('div', class_='cell profile__detailwrapper')
                for wrapper in detail_wrappers:
                    header = wrapper.find('h3', class_='profile__detail')
                    if header and 'Interests and hobbies' in header.text:
                        p_tag = wrapper.find('p')
                        if p_tag:
                            interests_and_hobbies = p_tag.text.strip()
                    elif header and 'Skills' in header.text:
                        p_tag = wrapper.find('p')
                        if p_tag:
                            skills = p_tag.text.strip()

                # Extract metrics
                def get_metric_value(title):
                    metrics = soup.find_all('div', class_='cell small-2 resultscard__metric')
                    for metric in metrics:
                        img = metric.find('img', title=title)
                        if img and metric.find('p'):
                            return metric.find('p').text.strip()
                    return "Not found"

                metrics = {
                    'mother_ethnic_origin': get_metric_value('Ethnic Origin Of Mother'),
                    'father_ethnic_origin': get_metric_value('Ethnic Origin Of Father'),
                    'donor_race': get_metric_value('Race'),
                    'skin_tone': get_metric_value('Skin Tone'),
                    'eye_color': get_metric_value('Eye Colour'),
                    'hair_color': get_metric_value('Hair Colour'),
                    'height': get_metric_value('Height'),
                    'weight': get_metric_value('Weight'),
                    'education': get_metric_value('Qualification'),
                    'occupation': get_metric_value('Occupation'),
                    'nationality': get_metric_value('Nationality'),
                    'religion': get_metric_value('Religion')
                }

                # Return all extracted data
                return {
                    'url': full_url,
                    'donor_id': donor_id,
                    'donor_description': donor_description,
                    'donor_quote': donor_quote,
                    'interests_and_hobbies': interests_and_hobbies,
                    'skills': skills,
                    **metrics,
                }
            else:
                logger.error(f"URL: {full_url} does not contain a valid profile.")
                return None
        else:
            logger.error(f"URL: {full_url} returned status code {response.status_code}.")
            return None
            
    except Exception as e:
        logger.error(f"Error scraping profile {full_url}: {str(e)}")
        return None

def main():
    # Load configuration
    global config, bank_config
    config = load_config()
    bank_id = 'bank2'
    bank_config = config['banks'][bank_id]

    # Initialize session
    global session
    session = requests.Session()

    # Perform Login
    try:
        logger.info(f"Starting login process for {bank_config['name']}...")
        login_successful = login(session, config, bank_id)
        
        if login_successful:
            logger.info("Successfully logged in and reached dashboard")
        else:
            logger.error("Failed to login - check credentials and website status")
            raise Exception("Login failed")
    except Exception as e:
        logger.error(f"An unexpected error occurred: {str(e)}")
        raise

    # Scrape Profiles
    all_profiles_bank2 = []
    try:
        for page in range(1, bank_config['max_pages'] + 1):
            logger.info(f"Scraping page {page}")
            
            profile_links = get_profile_links(session, page)
            logger.info(f"Found {len(profile_links)} profiles on page {page}")
            
            for relative_url in profile_links:
                logger.info(f"Scraping profile: {relative_url}")
                
                profile_data = scrape_profile(relative_url)
                if profile_data:
                    all_profiles_bank2.append(profile_data)
                    logger.info(f"Successfully scraped profile {profile_data.get('donor_id', 'unknown')}")
                
                time.sleep(random.uniform(2, 4))
    except Exception as e:
        logger.error(f"Error during scraping: {str(e)}")
        raise

    # Save Data
    if all_profiles_bank2:
        try:
            # Ensure output directory exists
            os.makedirs(config['output_directory'], exist_ok=True)
            
            # Save as JSON
            json_filename = os.path.join(config['output_directory'], f'profiles_{bank_id}.json')
            with open(json_filename, 'w', encoding='utf-8') as f:
                json.dump(all_profiles_bank2, f, indent=2, ensure_ascii=False)
            logger.info(f"Data saved to {json_filename}")
            
            # Save as CSV
            csv_filename = os.path.join(config['output_directory'], f'profiles_{bank_id}.csv')
            if all_profiles_bank2:
                with open(csv_filename, 'w', newline='', encoding='utf-8') as f:
                    writer = csv.DictWriter(f, fieldnames=all_profiles_bank2[0].keys())
                    writer.writeheader()
                    writer.writerows(all_profiles_bank2)
            logger.info(f"Data saved to {csv_filename}")
        except Exception as e:
            logger.error(f"Error saving data: {str(e)}")
            raise
    else:
        logger.warning("No profiles were collected to save")

if __name__ == "__main__":
    main()