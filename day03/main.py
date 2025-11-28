import re


def part1(input_data):
    total = 0

    mul_pattern = r"mul\((-?\d+),(-?\d+)\)"
    matches = re.findall(mul_pattern, input_data)

    for x_str, y_str in matches:
        x = int(x_str)
        y = int(y_str)
        total += x * y

    return total


def part2(input_data):
    total = 0

    return total


if __name__ == "__main__":
    input_data = open("input.txt").read().strip()
    print(f"Part 1: {part1(input_data)}")
    print(f"Part 2: {part2(input_data)}")
