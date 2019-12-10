"""
Calculate the total fuel requirement for Santa's rocket
"""

import math


def calculate_module_fuel_simple(mass: int) -> int:
    """ calculate the fuel requirement for a single module """
    return math.floor(mass / 3) - 2


def calculate_module_fuel(mass: int) -> int:
    """ calculate the fuel requirement for a single module """
    module_fuel = calculate_module_fuel_simple(mass)

    # calculate the fuel required for the fuel needed for the module
    if module_fuel <= 0:
        return 0
    else:
        iter_fuel = calculate_module_fuel(module_fuel)
        module_fuel += iter_fuel

    return module_fuel


def calculate_total_fuel(input_file: str) -> None:
    """ calculate the fuel required for all modules in the spacecraft """
    total_fuel_simple = 0
    total_fuel = 0
    with open(input_file, 'r') as reader:
        for line in reader.readlines():
            module_mass = int(line)
            module_fuel_simple = calculate_module_fuel_simple(module_mass)
            total_fuel_simple += module_fuel_simple

            module_fuel = calculate_module_fuel(module_mass)
            total_fuel += module_fuel

    print(f"Total Fuel (Part 1): {total_fuel_simple}")
    print(f"Total Fuel (Part 2): {total_fuel}")


if __name__ == "__main__":
    calculate_total_fuel("input.txt")
