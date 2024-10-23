from bs4 import BeautifulSoup
import logging
import random
import time
from log_utils import setup_anonymized_logging

logger = setup_anonymized_logging()

def get_headers(user_agents, bank_info):
    """
    Generate headers with a random user agent.
    
    Args:
        user_agents (list): List of user agent strings
        bank_info (dict): Bank-specific configuration
    """
    return {
        'User-Agent': random.choice(user_agents),
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'DNT': '1',
        'Referer': bank_info['login_url'],
        'sec-ch-ua': '"Google Chrome";v="119"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"'
    }

def login(session, config, bank_id='bank2'):
    """
    Attempt to login to the website.
    
    Args:
        session: requests.Session object
        config (dict): Configuration dictionary containing all settings
        bank_id (str): ID of the bank to login to (default: 'bank2' for London Sperm Bank)
    
    Returns:
        bool: True if login successful, False otherwise
    """
    try:
        # Get bank-specific configuration
        bank_info = config['banks'][bank_id]
        credentials = config['shared_credentials']
        user_agents = config['user_agents']
        
        # Add trailing slash if missing
        login_url = bank_info['login_url']
        if not login_url.endswith('/'):
            login_url = login_url + '/'
            
        # Set up session headers
        session.headers.update(get_headers(user_agents, bank_info))
        
        # Initial delay
        time.sleep(2)
        
        # Get the login page
        logger.info(f"Fetching login page for {bank_info['name']}: {login_url}")
        response = session.get(login_url, allow_redirects=True)
        response.raise_for_status()
        
        # Short delay after getting the page
        time.sleep(1)
        
        # Parse the page
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Debug: Save the HTML content
        with open('login_page_debug.html', 'w', encoding='utf-8') as f:
            f.write(response.text)
        
        # Try multiple strategies to find the login form
        login_form = None
        all_forms = soup.find_all('form')
        logger.info(f"Found {len(all_forms)} forms on the page")
        
        # Strategy 1: Find by class
        login_form = soup.find('form', {'class': 'login__form'})
        
        # Strategy 2: Find form with EmailAddress input
        if not login_form:
            for form in all_forms:
                if form.find('input', {'id': 'EmailAddress'}):
                    login_form = form
                    break
        
        # Strategy 3: Find form with Password input
        if not login_form:
            for form in all_forms:
                if form.find('input', {'id': 'Password'}):
                    login_form = form
                    break
        
        if not login_form:
            logger.error("Could not find login form")
            logger.info(f"Forms found on page: {[f.get('class', 'No class') for f in all_forms]}")
            return False
            
        # Get the verification token
        token_input = soup.find('input', {'name': '__RequestVerificationToken'})
        if not token_input:
            logger.error("Could not find __RequestVerificationToken")
            return False
            
        token = token_input.get('value')
        if not token:
            logger.error("Verification token has no value")
            return False
        
        # Prepare login data
        login_data = {
            'EmailAddress': credentials['username'],
            'Password': credentials['password'],
            '__RequestVerificationToken': token,
            'RememberMe': 'true'
        }
        
        # Get the form's method and action
        form_method = login_form.get('method', 'post')
        form_action = login_form.get('action', '')
        
        # Construct the form action URL
        if not form_action:
            form_action = login_url
        elif not form_action.startswith('http'):
            if form_action.startswith('/'):
                form_action = bank_info['base_url'] + form_action
            else:
                form_action = bank_info['base_url'] + '/' + form_action
        
        # Update headers for the form submission
        session.headers.update({
            'Content-Type': 'application/x-www-form-urlencoded',
            'Origin': bank_info['base_url'],
            'Referer': login_url,
            'Cache-Control': 'no-cache',
            'Pragma': 'no-cache'
        })
        
        # Small delay before posting
        time.sleep(1)
        
        # Attempt login
        logger.info(f"Attempting login to: {form_action}")
        logger.info(f"Using method: {form_method}")
        logger.info(f"Form data (excluding password): {dict(EmailAddress=login_data['EmailAddress'], __RequestVerificationToken=login_data['__RequestVerificationToken'])}")
        
        response = session.post(
            form_action,
            data=login_data,
            allow_redirects=True
        )
        response.raise_for_status()
        
        # Check if we were redirected to the dashboard
        dashboard_url = f"{bank_info['base_url']}/catalogue/user/dashboard/"
        current_url = response.url
        
        logger.info(f"Final URL after login attempt: {current_url}")
        
        if dashboard_url in current_url:
            logger.info(f"Login successful for {bank_info['name']} - Redirected to dashboard")
            return True
        else:
            logger.error(f"Login failed for {bank_info['name']} - Not redirected to dashboard. Current URL: {current_url}")
            return False
                
    except Exception as e:
        logger.error(f"Login failed with error: {str(e)}")
        return False