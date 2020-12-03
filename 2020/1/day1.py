"""
Advent of Code 2020 - day 1: https://adventofcode.com/2020/day/1
Report Repair
"""
import itertools
import math

def repair(numbers: list, setsize: int) -> None:
    """ Find the setsize combination of numbers that add to 2020 and multiply them """
    for subset in itertools.combinations(numbers, setsize):
        total = sum(subset)
        if total == 2020:
            print(f"{math.prod(subset)}")
            break

def scour_report(input_file: str) -> None:
    """ check a report for numbers that add to 2020 and multiply them """
    numbers = []
    with open(input_file, 'r') as reader:
        for line in reader.readlines():
            numbers.append(int(line))

    repair(numbers, 2)
    repair(numbers, 3)


if __name__ == "__main__":
    scour_report("input.txt")
