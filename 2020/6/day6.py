"""
Advent of Code 2020 - day 6: https://adventofcode.com/2020/day/6
Custom Customs
"""

def part1(forms: list) -> None:
    """ Determine any form question marked "yes" for each group """
    total = 0
    for form in forms:
        form_set = set()
        for entry in form:
            form_set.update(entry)

        total += len(form_set)

    print(f"Sum of Anyone: {total}")


def part2(forms: list) -> None:
    """ Determine every form question marked "yes" for each group """
    total = 0
    for form in forms:
        form_set = {*form[0]}
        for entry in form:
            form_set = form_set.intersection(entry)

        total += len(form_set)

    print(f"Sum of Everyone: {total}")


def main(input_file: str) -> None:
    """ parse input & run analysis """
    forms = []
    with open(input_file, 'r') as reader:
        index = 0
        for line in reader:
            line = list(line.strip())
            if not line:
                index += 1
                continue

            try:
                forms[index].append(line)
            except IndexError:
                forms.append([line])

    part1(forms)
    part2(forms)


if __name__ == "__main__":
    main("input.txt")
