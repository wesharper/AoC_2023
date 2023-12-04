from os import path


def get_input_file_lines() -> list[str]:
    with open(path.join(path.dirname(__file__), "input.txt"), "r") as input_file:
        return input_file.readlines()


def part_one():
    lines = get_input_file_lines()

    total = 0
    for line in lines:
        left = right = None
        # find leftmost digit
        for char in line:
            if char.isdigit():
                left = char
                break
        # find rightmost digit
        for char in reversed(line):
            if char.isdigit():
                right = char
                break

        # add number to total
        total += int(f"{left}{right}")

    return total


# print(part_one())


def part_two():
    lines = get_input_file_lines()
    digits = [
        ('zero', 0),
        ('one', 1),
        ('two', 2),
        ('three', 3),
        ('four', 4),
        ('five', 5),
        ('six', 6),
        ('seven', 7),
        ('eight', 8),
        ('nine', 9)
    ]

    total = 0
    for line in lines:
        left = right = None
        # find leftmost digit
        for index, char in enumerate(line):
            if left is not None:
                break
            if char.isdigit():
                left = int(char)
                break
            for name, val in digits:
                substring = line[index:len(name) + index]
                if substring.find(name) != -1:
                    left = val
                    break

        # find rightmost digit
        for index, char in enumerate(reversed(line)):
            if right is not None:
                break
            if char.isdigit():
                right = int(char)
                break
            for name, val in digits:
                reversed_line = line[::-1]
                reversed_name = name[::-1]

                substring = reversed_line[index:len(reversed_name) + index]
                if substring.find(reversed_name) != -1:
                    right = val
                    break

        total += int(f"{left}{right}")

    return total


print(part_two())
