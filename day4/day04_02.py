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
            try:
                passport.update({piece[0]: int(piece[1])})
            except:
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
            "byr": {"type": "number", "minimum": 1920, "maximum": 2002},
            "iyr": {"type": "number", "minimum": 2010, "maximum": 2020},
            "eyr": {"type": "number", "minimum": 2020, "maximum": 2030},
            "hgt": {"type": "string", "pattern": "^1(5\d|[6-8]\d|9[0-3])cm|(59|6\d|7[0-6])in$"},
            "hcl": {"type": "string", "pattern": "^#[A-Fa-f0-9]{6}$"},
            "ecl": {"type": "string", "enum": ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]},
            "pid": {"type": "number", "minimum": 1, "maximum": 999999999},
            "cid": {"type": "number"},
        },
        "additionalProperties": False,
        "required": ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"],
    }
    for passport in passports:
        try:
            jsonschema.validate(instance=passport, schema=schema)
            validCount += 1
            logger.debug(f"Passport OK: {passport}")
            logger.info(f"Passport Valid: All checks OK ({validCount})")
        except jsonschema.exceptions.ValidationError as error:
            logger.debug(f"Passport Invalid: {passport}")
            logger.error(f"Passport Invalid: {error.message}")
    # Off by one for some damned reason
    # If anyone see this and knows why tell me
    logger.info(f"Solution: {validCount}")

if __name__ == '__main__':
    main()