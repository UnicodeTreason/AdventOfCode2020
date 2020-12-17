#!/usr/bin/env python3
import logging
import os

# Module constants
DIR_BASE  = os.path.dirname(__file__)
DIR_ETC   = f'{DIR_BASE}'
DIR_VAR   = f'{DIR_BASE}'
FILE_NAME = os.path.basename(__file__)

# Configure Logging
# Configured with a Console and File handler for convenience
formatter = logging.Formatter('%(asctime)s|%(name)s|%(levelname)s|%(message)s')
log_handler_console = logging.StreamHandler()
log_handler_console.setLevel(logging.INFO)
log_handler_console.setFormatter(formatter)

log_handler_file = logging.FileHandler(f"{DIR_VAR}/{FILE_NAME}.log")
log_handler_file.setLevel(logging.DEBUG)
log_handler_file.setFormatter(formatter)

logger = logging.getLogger(FILE_NAME)
logger.setLevel(logging.DEBUG)
logger.addHandler(log_handler_console)
logger.addHandler(log_handler_file)

def main():
    logger.info(f"Starting Day 1")

    logger.info(f"Exiting Day 1")

if __name__ == '__main__':
    main()