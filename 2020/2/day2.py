"""
Advent of Code 2020 - day 2: https://adventofcode.com/2020/day/2
Password Philosophy
"""

def part1(pair: dict) -> bool:
    """
    check if password meets policy: between min & max numbers
    of required character
    """
    occurrences = pair["password"].count(pair["policy"]["char"])
    if pair["policy"]["min"] <= occurrences <= pair["policy"]["max"]:
        return True

    return False


def part2(pair: dict) -> bool:
    """
    check if password meets policy: need one (and only one) of character
    at positions specified in policy
    """
    char = pair["policy"]["char"]
    password = pair["password"]
    if (password[pair["policy"]["min"]] == char) ^ (password[pair["policy"]["max"]] == char):
        return True

    return False


def check_passwords(input_file: str) -> None:
    """ check a list of passwords against their policies """
    password_sets = []
    with open(input_file, 'r') as reader:
        for line in reader.readlines():
            policy_text, sep, password = line.partition(':')
            constraint, sep, char = policy_text.partition(' ')
            lower, sep, upper = constraint.p('-')

            pair = {
                "policy": {
                    "min": int(lower),
                    "max": int(upper),
                    "char": char
                },
                "password": password.rstrip()
            }
            password_sets.append(pair)

    validp1 = 0
    validp2 = 0
    for pair in password_sets:
        if part1(pair):
            validp1 += 1
        if part2(pair):
            validp2 += 1

    print(f"Valid passwords (part 1): {validp1}")
    print(f"Valid passwords (part 2): {validp2}")


if __name__ == "__main__":
    check_passwords("input.txt")
