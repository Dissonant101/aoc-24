import re


def part1(input_data):
    total = 0
    regex_pattern = r"mul\((-?\d+),(-?\d+)\)"
    matches = re.findall(regex_pattern, input_data)

    for x_str, y_str in matches:
        x = int(x_str)
        y = int(y_str)
        total += x * y

    return total


def part2(input_data):
    total = 0
    regex_pattern = r"(do\(\))|(don't\(\))|(mul\((-?\d+),(-?\d+)\))"
    matches = re.findall(regex_pattern, input_data)
    state = True

    for match in matches:
        if match[0]:  # do()
            state = True
        elif match[1]:  # don't()
            state = False
        elif match[2]:  # mul(x,y)
            if state:
                total += int(match[3]) * int(match[4])

    return total


if __name__ == "__main__":
    input_data = open("input.txt").read().strip()
    print(f"Part 1: {part1(input_data)}")
    print(f"Part 2: {part2(input_data)}")
