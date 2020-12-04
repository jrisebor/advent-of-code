"""
Advent of Code 2020 - day 4: https://adventofcode.com/2020/day/4
Passport Processing
"""
import re

def parse_input(raw_input: list) -> list:
    """ Turn the raw passport input data into a list of passports """
    index = 0
    passports = []
    for line in raw_input:
        if not line:
            index += 1

        try:
            passports[index].extend(line)
        except IndexError:
            passports.append(line)

    for index, item in enumerate(passports):
        passport = {}
        for entry in item:
            field, sep, value = entry.partition(':')
            passport[field] = value

        passports[index] = passport


    return passports

def validate_fields(passports: list) -> int:
    """ Return the number of passports with all required fields """
    valid = 0
    required_keys = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    for passport in passports:
        if all(key in passport for key in required_keys):
            valid += 1

    return valid


def valid_year(year: int, min_year: int, max_year: int) -> bool:
    """ Determine if the year input is valid, give min & max """
    if (len(str(year)) == 4) and (max_year >= int(year) >= min_year):
        return True

    return False


def valid_height(raw_height: str) -> bool:
    """ Determine if the height is valid """
    cm_max = 193
    cm_min = 150
    in_max = 76
    in_min = 59
    split = re.match(r"([0-9]+)([a-z]+)", raw_height, re.I)
    if split:
        height = split.groups()
    else:
        return False

    if height[1] == "cm":
        if cm_max >= int(height[0]) >= cm_min:
            return True
    elif height[1] == "in":
        if in_max >= int(height[0]) >= in_min:
            return True

    return False


def validate_data(passports: list) -> int:
    """ Return the number of passports with valid data """
    valid = 0
    for passport in passports:
        try:
            if not valid_year(passport["byr"], 1920, 2002):
                continue
            if not valid_year(passport["iyr"], 2010, 2020):
                continue
            if not valid_year(passport["eyr"], 2020, 2030):
                continue
            if not valid_height(passport["hgt"]):
                continue
            if not re.search(r'^#(?:[0-9a-fA-F]{3}){1,2}$', passport["hcl"]):
                continue
            if passport["ecl"] not in ("amb", "blu", "brn", "gry", "grn", "hzl", "oth"):
                continue
            if len(str(passport["pid"])) != 9:
                continue
            valid += 1
        except KeyError:
            continue

    return valid


def count_valid_passports(input_file: str) -> None:
    """ Determine how many passports are valid """
    raw_input = []
    with open(input_file, 'r') as reader:
        for line in reader.readlines():
            raw_input.append(line.strip().split())

    passports = parse_input(raw_input)
    valid = validate_fields(passports) # part 1
    print(f"Valid Passports (part 1): {valid}")
    valid = validate_data(passports) # part 2
    print(f"Valid Passports (part 2): {valid}")


if __name__ == "__main__":
    count_valid_passports("input.txt")
