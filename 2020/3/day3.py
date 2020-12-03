"""
Advent of Code 2020 - day 3: https://adventofcode.com/2020/day/3
Toboggan Trajectory
"""

def ride(area_map: list, right: int, down: int) -> int:
    """ traverse area map with given slope """
    collisions = 0
    index = 0
    width = len(area_map[0])
    for line in area_map[::down]:
        wrapped_index = index % width
        if line[wrapped_index] == '#':
            collisions += 1
        index += right

    print(f"Collisions for pattern right {right}, down {down}: {collisions}")
    return collisions


def map_trajectory(input_file: str) -> None:
    """ Determine the path of the toboggan """
    area_map = []
    with open(input_file, 'r') as reader:
        for line in reader.readlines():
            area_map.append(list(line.strip()))

    product = ride(area_map, 1, 1)
    product *= ride(area_map, 3, 1) # part 1
    product *= ride(area_map, 5, 1)
    product *= ride(area_map, 7, 1)
    product *= ride(area_map, 1, 2)

    print(f"Product: {product}")


if __name__ == "__main__":
    map_trajectory("input.txt")
