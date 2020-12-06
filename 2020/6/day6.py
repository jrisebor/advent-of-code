"""
Advent of Code 2020 - day 6: https://adventofcode.com/2020/day/6
Custom Customs
"""

forms = []
with open("exampleinput.txt", 'r') as reader:
    index = 0
    for line in reader:
        line = list(line.strip())
        if not line:
            index += 1

        try:
            forms[index].update(line)
        except IndexError:
            forms.append(set(line))

print(f"Sum of Counts: {sum([len(form) for form in forms])}") # part 1
