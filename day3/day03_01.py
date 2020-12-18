#!/usr/bin/env python3
import logging
import os
import re
import sys
import time

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

def double_list_width(data):
    outData = []
    for line in data:
        outData.append(f"{line}{line}")
    return outData

def find_path(data):
    posx = 3
    posy = 1
    trees = 0

    for y in range(len(data)):
        line = data[y]
        for x in range(len(line)):
            if posx >= len(line):
                raise Exception("Edge Hit")

            if y == posy and x == posx:
                posx += 3
                posy += 1
                if line[x] == '#':
                    # print('X', end='')
                    trees += 1
                # else:
                    # print('O', end='')
            # else:
                # print(line[x], end='')
        # print()

    return trees

def main():
    logger.info(f"Starting Day 3")
    logger.info(f"Import data")
    fData = data_import('day03', 'prod')

    logger.info(f"Process data")
    trees = 0
    while trees == 0:
        fData = double_list_width(fData)
        try:
            trees = find_path(fData)
        except KeyboardInterrupt:
            sys.exit()
        except:
            logger.error(f"Edge Hit - Doubling Field Width")

    logger.info(f"Trees: {trees}")

if __name__ == '__main__':
    main()