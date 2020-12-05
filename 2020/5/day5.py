"""
Advent of Code 2020 - day 5: https://adventofcode.com/2020/day/5
Binary Boarding
"""

def decode_pass(seat: str) -> int:
    lower_rows, upper_rows = 0, 127
    lower_columns, upper_columns = 0, 7
    row, column = 0, 0
    for step in list(seat):
        if step == "F":
            upper_rows = int((upper_rows - lower_rows) / 2) + lower_rows
        elif step == "B":
            lower_rows = int((upper_rows - lower_rows) / 2) + lower_rows +1
        elif step == "L":
            upper_columns = int((upper_columns - lower_columns) / 2) + lower_columns
        elif step == "R":
            lower_columns = int((upper_columns - lower_columns) / 2) + lower_columns + 1

    return lower_rows * 8 + lower_columns


def boarding(input_file: str) -> None:
    """ Determine seat ID """
    boarding_passes = []
    with open(input_file, 'r') as reader:
        for line in reader.readlines():
            boarding_passes.append(list(line.strip()))

    highest = 0
    for seat in boarding_passes:
        seat_id = decode_pass(seat)
        if seat_id > highest:
            highest = seat_id

    print(f"Highest Seat ID: {highest}")

if __name__ == "__main__":
    boarding("input.txt")
