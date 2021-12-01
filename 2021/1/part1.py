"""
Advent of Code 2021 - day 1: https://adventofcode.com/2021/day/1
Sonar Sweep
"""
depth_increases = 0
last = 0
with open("input.txt", 'r') as reader:
    for line in reader.readlines():
        current = int(line)
        if current > last:
            depth_increases += 1

        last = current

print(f"Number of Increases: {depth_increases - 1}")
