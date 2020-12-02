"""
Advent of Code 2020 - day 2: https://adventofcode.com/2020/day/2
Password Philosophy
"""

def validate(pair: dict) -> bool:
    occurrences = pair["password"].count(pair["policy"]["char"])
    if pair["policy"]["min"] <= occurrences <= pair["policy"]["max"]:
        return True

    return False


def check_passwords(input_file: str) -> None:
    """ check a list of passwords against their policies """
    input = []
    with open(input_file, 'r') as reader:
        for line in reader.readlines():
            policy_text,sep,password = line.partition(':')
            constraint,sep,char = policy_text.partition(' ')
            lower,sep,upper = constraint.partition('-')

            pair = {
                "policy": {
                    "min": int(lower),
                    "max": int(upper),
                    "char": char
                },
                "password": password.rstrip()
            }
            input.append(pair)
    
    valid = 0
    for pair in input:
        if validate(pair):
            valid += 1

    print(f"Valid passwords: {valid}")


if __name__ == "__main__":
    check_passwords("input.txt")
