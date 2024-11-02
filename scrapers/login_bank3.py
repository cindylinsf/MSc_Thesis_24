# login_bank3.py

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, ElementNotInteractableException
from selenium.webdriver.common.action_chains import ActionChains
import logging
import random
import time
from log_utils import setup_anonymized_logging

logger = setup_anonymized_logging()

def setup_driver():
    """
    Configure and return a Chrome WebDriver instance
    """
    options = webdriver.ChromeOptions()
    options.add_argument('--disable-blink-features=AutomationControlled')
    options.add_argument('--start-maximized')
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    
    return webdriver.Chrome(options=options)

def save_screenshot(driver, name):
    """
    Save a screenshot for debugging
    """
    try:
        driver.save_screenshot(f'debug_{name}.png')
        logger.info(f"Saved screenshot: debug_{name}.png")
    except Exception as e:
        logger.error(f"Failed to save screenshot: {str(e)}")

def navigate_to_login(driver, bank_info):
    """
    Navigate to the login page by finding and clicking the login button
    """
    try:
        logger.info("Looking for login button...")
        # Try multiple selectors for the login button
        selectors = [
            (By.XPATH, "//a[text()='Login']"),
            (By.XPATH, "//button[contains(@class, 'Login')]"),
            (By.CSS_SELECTOR, ".ct-link-button.login"),
            (By.CLASS_NAME, "login"),
            (By.LINK_TEXT, "Login")
        ]
        
        wait = WebDriverWait(driver, 10)
        login_button = None
        
        for by, selector in selectors:
            try:
                login_button = wait.until(
                    EC.element_to_be_clickable((by, selector))
                )
                break
            except:
                continue
                
        if login_button:
            logger.info("Found login button, clicking...")
            driver.execute_script("arguments[0].scrollIntoView(true);", login_button)
            time.sleep(1)
            login_button.click()
            time.sleep(3)
            return True
        else:
            logger.error("Could not find login button")
            save_screenshot(driver, "no_login_button")
            return False
            
    except Exception as e:
        logger.error(f"Error navigating to login: {str(e)}")
        save_screenshot(driver, "nav_error")
        return False

def login(driver, config, bank_id='bank3'):
    """
    Attempt to login to bank3 website using Selenium WebDriver
    """
    try:
        bank_info = config['banks'][bank_id]
        credentials = config['shared_credentials']
        
        # Navigate to the main site first
        logger.info("Navigating to main site...")
        driver.get(bank_info['base_url'])
        time.sleep(3)
        save_screenshot(driver, "main_page")
        
        # Navigate to login page by clicking the login button
        if not navigate_to_login(driver, bank_info):
            logger.error("Failed to navigate to login page")
            return False
            
        save_screenshot(driver, "login_page")
        
        # Look for login form fields using multiple selectors
        logger.info("Looking for login form fields...")
        wait = WebDriverWait(driver, 10)
        
        # Try multiple selectors for username field
        username_selectors = [
            (By.NAME, "log"),
            (By.CSS_SELECTOR, "input[name='log']"),
            (By.ID, "user_login"),
            (By.CSS_SELECTOR, ".tml-user-login-wrap input")
        ]
        
        username_field = None
        for by, selector in username_selectors:
            try:
                username_field = wait.until(
                    EC.presence_of_element_located((by, selector))
                )
                break
            except:
                continue
                
        if not username_field:
            logger.error("Could not find username field")
            save_screenshot(driver, "no_username_field")
            return False
            
        # Try multiple selectors for password field
        password_selectors = [
            (By.NAME, "pwd"),
            (By.CSS_SELECTOR, "input[name='pwd']"),
            (By.ID, "user_pass"),
            (By.CSS_SELECTOR, ".tml-user-pass-wrap input")
        ]
        
        password_field = None
        for by, selector in password_selectors:
            try:
                password_field = wait.until(
                    EC.presence_of_element_located((by, selector))
                )
                break
            except:
                continue
                
        if not password_field:
            logger.error("Could not find password field")
            save_screenshot(driver, "no_password_field")
            return False
            
        # Clear fields and enter credentials
        username_field.clear()
        password_field.clear()
        
        logger.info("Entering credentials...")
        username_field.send_keys(credentials['username'])
        time.sleep(random.uniform(0.5, 1.0))
        password_field.send_keys(credentials['password'])
        
        # Look for login submit button
        submit_selectors = [
            (By.NAME, "wp-submit"),
            (By.CSS_SELECTOR, "input[type='submit']"),
            (By.CSS_SELECTOR, "button[type='submit']"),
            (By.CSS_SELECTOR, ".tml-submit-wrap input"),
            (By.XPATH, "//input[@value='Log In']")
        ]
        
        submit_button = None
        for by, selector in submit_selectors:
            try:
                submit_button = wait.until(
                    EC.element_to_be_clickable((by, selector))
                )
                break
            except:
                continue
                
        if not submit_button:
            logger.error("Could not find submit button")
            save_screenshot(driver, "no_submit_button")
            return False
            
        logger.info("Clicking submit button...")
        driver.execute_script("arguments[0].scrollIntoView(true);", submit_button)
        time.sleep(1)
        submit_button.click()
        
        # Wait for redirect and check result
        time.sleep(5)
        save_screenshot(driver, "after_submit")
        
        if "my-account" in driver.current_url:
            logger.info("Login successful!")
            return True
        else:
            logger.error(f"Login failed - Current URL: {driver.current_url}")
            return False
            
    except Exception as e:
        logger.error(f"Login failed with error: {str(e)}")
        logger.exception("Full traceback:")
        save_screenshot(driver, "error")
        return False

def cleanup_driver(driver):
    """
    Properly close the WebDriver
    """
    try:
        driver.quit()
    except:
        pass