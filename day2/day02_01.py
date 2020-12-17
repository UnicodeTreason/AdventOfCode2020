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
        #Split useful data out of line then count chars
        match = re.match(r'^(?P<rulemin>\d+)-(?P<rulemax>\d+) (?P<rulefilter>\w+): (?P<password>\w+)$', line)
        password = match.group('password')
        rule_min = int(match.group('rulemin'))
        rule_max = int(match.group('rulemax'))
        count = int(match.group('password').count(match.group('rulefilter')))
        if count >= rule_min and count <= rule_max:
            valid_pwd_count += 1

    logger.info(f"Valid Passwords: {valid_pwd_count}")

if __name__ == '__main__':
    main()