import json
import logging  
from log_utils import setup_anonymized_logging

logger = setup_anonymized_logging()

def load_config(config_file='config.json'):
    try:
        with open(config_file, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        logger.error(f"Configuration file {config_file} not found.")
        exit(1)
    except json.JSONDecodeError:
        logger.error(f"Error parsing {config_file}. Please check its format.")
        exit(1)