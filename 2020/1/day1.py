"""
Advent of Code 2020 - day 1: https://adventofcode.com/2020/day/1
Report Repair
"""
import itertools

def part1(numbers: list) -> None:
    for subset in itertools.combinations(numbers, 2):
        total = sum(subset)
        if total == 2020:
            print(f"{subset[0]*subset[1]}")
            break


def scour_report(input_file: str) -> None:
    """ check a report for numbers that add to 2020 and multiply them """
    numbers = []
    with open(input_file, 'r') as reader:
        for line in reader.readlines():
            numbers.append(int(line))
    
    part1(numbers)




if __name__ == "__main__":
    scour_report("input.txt")
