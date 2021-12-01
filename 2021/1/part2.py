"""
Advent of Code 2021 - day 1: https://adventofcode.com/2021/day/1
Sonar Sweep
"""
depth_increases = 0
last = 0
window = []
with open("input.txt", 'r') as reader:
    for line in reader.readlines():
        window.append(int(line))
        if len(window) < 3:
            continue

        current = sum(window)
        if current > last:
            depth_increases += 1

        last = current
        window.pop(0)

print(f"Number of Increases: {depth_increases - 1}")
