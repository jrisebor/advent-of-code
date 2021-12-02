"""
Advent of Code 2021 - day 2: https://adventofcode.com/2021/day/2
Dive!
"""
x, y = 0, 0
with open("input.txt", 'r') as reader:
    for line in reader.readlines():
        command = line.split()
        direction, magnitude = command[0], int(command[1])
        if direction == "forward":
            x += magnitude
        elif direction == "down":
            y += magnitude
        elif direction == "up":
            y -= magnitude
        else:
            print("unknown command")

print(f"Position x Depth = {x * y}")
