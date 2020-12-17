#!/usr/bin/env python3
import logging
import os
import re
import sys

# Module constants
DIR_BASE  = os.path.dirname(__file__)
FILE_NAME = os.path.basename(__file__)

# Configure Logging
formatter = logging.Formatter('%(asctime)s|%(name)s|%(levelname)s|%(message)s')
log_handler_console = logging.StreamHandler()
log_handler_console.setLevel(logging.DEBUG)
log_handler_console.setFormatter(formatter)
logger = logging.getLogger(FILE_NAME)
logger.setLevel(logging.INFO)
logger.addHandler(log_handler_console)

def data_import(file, environment):
    logger.debug(f"function start: {sys._getframe(  ).f_code.co_name}")
    fData = open(f"{DIR_BASE}/{file}.{environment}", "r")
    fDataRAW = fData.readlines()
    fDataClean = []
    count = 0

    for line in fDataRAW:
        fDataClean.append(line.strip())
        logger.debug(f"Line{count}: {line.strip()}")
        count += 1

    return fDataClean

def main():
    logger.info(f"Starting Day 2")
    logger.info(f"Import data")
    fData = data_import('day02', 'prod')

    logger.info(f"Process data")
    valid_pwd_count = 0
    for line in fData:
        # Split useful data out of line then check indexs
        match = re.match(r'^(?P<index1>\d+)-(?P<index2>\d+) (?P<rulefilter>\w+): (?P<password>\w+)$', line)
        password = match.group('password')
        index1 = int(match.group('index1'))
        index2 = int(match.group('index2'))
        rulefilter = match.group('rulefilter')

        # Check with XOR, only 1 can be True to be Valid
        if (password[index1-1] == rulefilter) ^ (password[index2-1] == rulefilter):
            valid_pwd_count += 1

    logger.info(f"Valid Passwords: {valid_pwd_count}")

if __name__ == '__main__':
    main()