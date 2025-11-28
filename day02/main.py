from itertools import pairwise


def part1(input_data):
    def is_safe(nums):
        if nums[0] < nums[1]:
            return all(x < y and y - x <= 3 for x, y in pairwise(nums))
        else:
            return all(x > y and x - y <= 3 for x, y in pairwise(nums))

    def check_level(line):
        line_list = [int(n) for n in line.split()]
        return is_safe(line_list)

    count = 0

    for line in input_data.splitlines():
        count += 1 if check_level(line) else 0

    return count


def part2(input_data):
    def is_safe(nums):
        if nums[0] < nums[1]:
            return all(x < y and y - x <= 3 for x, y in pairwise(nums))
        else:
            return all(x > y and x - y <= 3 for x, y in pairwise(nums))

    def check_level(line):
        line_list = [int(n) for n in line.split()]

        if is_safe(line_list):
            return True

        for i in range(len(line_list)):
            modified_list = line_list[:i] + line_list[i + 1 :]

            if is_safe(modified_list):
                return True
        return False

    count = 0

    for line in input_data.splitlines():
        count += 1 if check_level(line) else 0

    return count


if __name__ == "__main__":
    input_data = open("input.txt").read().strip()
    print(f"Part 1: {part1(input_data)}")
    print(f"Part 2: {part2(input_data)}")
