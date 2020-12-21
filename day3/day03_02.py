#!/usr/bin/env python3
from functools import reduce
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
log_handler_console.setLevel(logging.INFO)
log_handler_console.setFormatter(formatter)

log_handler_file = logging.FileHandler(f"{DIR_BASE}/{FILE_NAME}.log")
log_handler_file.setLevel(logging.DEBUG)
log_handler_file.setFormatter(formatter)

logger = logging.getLogger(FILE_NAME)
logger.setLevel(logging.DEBUG)
logger.addHandler(log_handler_console)
logger.addHandler(log_handler_file)

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
    pathOptions = [
        {"right": 1, "down": 1},
        {"right": 3, "down": 1},
        {"right": 5, "down": 1},
        {"right": 7, "down": 1},
        {"right": 1, "down": 2}
    ]
    pathResults = []

    for index in range(len(pathOptions)):
        trees = 0
        posx = pathOptions[index]["right"]
        posy = pathOptions[index]["down"]
        logger.debug("--Staring Run--")
        for y in range(len(data)):
            line = data[y]
            lineOutput = ""
            for x in range(len(line)):
                if posx >= len(line):
                    raise Exception("Edge Hit")

                if y == posy and x == posx:
                    posx += pathOptions[index]["right"]
                    posy += pathOptions[index]["down"]
                    if line[x] == '#':
                        lineOutput += 'X'
                        trees += 1
                    else:
                        lineOutput += 'O'
                else:
                    lineOutput += line[x]
            logger.debug(lineOutput)
        pathResults.append(trees)

    # Multiply all results together for solution
    return reduce(lambda x, y: x*y, pathResults)

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
        except SystemExit:
            sys.exit()
        except:
            logger.error(f"Error: {sys.exc_info()}")

    logger.info(f"Trees: {trees}")

if __name__ == '__main__':
    main()