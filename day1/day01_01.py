#!/usr/bin/env python3
import logging
import os
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

def sum_for_2020(a: int, b: int):
    logger.debug(f"function start: {sys._getframe(  ).f_code.co_name}")
    logger.debug(f"params: {a}, {b}")
    # Skip if duplicate values, shouldn't check line against itself.
    if a == b:
        return int(-1)
    else:
        return int(a) + int(b)

def main():
    logger.info(f"Starting Day 1")
    logger.info(f"Import data")
    fData = data_import('day01', 'prod')

    logger.info(f"Process data")
    for i in range(len(fData)):
        for j in range(len(fData)):
            logger.debug(f"a: {fData[i]}, b: {fData[j]}")
            if sum_for_2020(fData[i], fData[j]) == 2020:
                logger.info(f"a: {fData[i]}, b: {fData[j]}")
                logger.info(f"Solution: {int(fData[i]) * int(fData[j])}")
                quit()

if __name__ == '__main__':
    main()