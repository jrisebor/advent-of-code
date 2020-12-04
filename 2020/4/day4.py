"""
Advent of Code 2020 - day 4: https://adventofcode.com/2020/day/4
Passport Processing
"""

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


def validate_passports(passports: list) -> int:
    """ Return the number of valid passports """
    valid = 0
    required_keys = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    for passport in passports:
        if all(key in passport for key in required_keys):
            valid += 1

    return valid



def count_valid_passports(input_file: str) -> None:
    """ Determine how many passports are valid """
    raw_input = []
    with open(input_file, 'r') as reader:
        for line in reader.readlines():
            raw_input.append(line.strip().split())

    passports = parse_input(raw_input)
    valid = validate_passports(passports)
    print(f"Valid Passports: {valid}")


if __name__ == "__main__":
    count_valid_passports("input.txt")
