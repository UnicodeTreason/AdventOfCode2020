#!/usr/bin/env python3
from functools import reduce
import json
import jsonschema
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
    passportCount = 0
    passports = []
    passport = {}

    for line in fData:
        logger.debug(f"Line: {line.strip()}")
        # If blank line, add current passport to dict and start new passport
        if line == "\n":
            passports.append(passport)
            passport = {}
            passportCount += 1
            continue

        # Split up line and get passport built
        phrase = (line.strip()).split(" ")
        for pieces in phrase:
            piece = pieces.split(":")
            passport.update({piece[0]: piece[1]})

    # Add last passport and close file
    passports.append(passport)
    fData.close()
    return passports

def main():
    logger.info(f"Starting Day 4")
    logger.info(f"Import data")
    passports = data_import('day04', 'prod')

    logger.info(f"Process data")
    validCount = 0
    schema = {
        "title": "Match Passport Data",
        "description": "This is a schema for matching passport data.",
        "type": "object",
        "properties": {
            "byr": {"type" : "string"},
            "iyr": {"type" : "string"},
            "eyr": {"type" : "string"},
            "hgt": {"type" : "string"},
            "hcl": {"type" : "string"},
            "ecl": {"type" : "string"},
            "pid": {"type" : "string"},
            "cid": {"type" : "string"},
        },
        "additionalProperties": False,
        "required": ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"],
    }
    for passport in passports:
        logger.debug(f"Checking Passport: {json.dumps(passport, indent=4)}")
        try:
            jsonschema.validate(instance=passport, schema=schema)
            validCount += 1
        except jsonschema.exceptions.ValidationError as error:
            logger.error(error.message)
    logger.info(f"Solution: {validCount}")

if __name__ == '__main__':
    main()