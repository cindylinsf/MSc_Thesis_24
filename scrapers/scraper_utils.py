# scraper_utils.py
import time
import random
from bs4 import BeautifulSoup
from log_utils import setup_anonymized_logging

logger = setup_anonymized_logging()

def add_random_delay(min_seconds=5, max_seconds=10):
    """Add random delay to mimic human behavior"""
    delay = random.uniform(min_seconds, max_seconds)
    time.sleep(delay)

def validate_response(response, expected_elements):
    """Validate if response contains expected HTML elements"""
    soup = BeautifulSoup(response.text, 'html.parser')
    return all(soup.find(elem['tag'], class_=elem.get('class')) 
              for elem in expected_elements)

def get_page_data(session, url, retries=3):
    """Get page data with retry logic"""
    for attempt in range(retries):
        try:
            response = session.get(url)
            response.raise_for_status()
            return response
        except Exception as e:
            logger.error(f"Attempt {attempt + 1} failed: {str(e)}")
            if attempt < retries - 1:
                add_random_delay(4, 6)  # Longer delay between retries
            else:
                raise