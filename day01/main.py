import heapq
from collections import Counter


def part1(input_data):
    left = []
    right = []
    distance = 0

    for line in input_data.splitlines():
        l, r = line.split()
        left_num = int(l)
        right_num = int(r)
        heapq.heappush(left, left_num)
        heapq.heappush(right, right_num)

    for _ in range(len(left)):
        distance += abs(heapq.heappop(left) - heapq.heappop(right))

    return distance


def part2(input_data):
    left = []
    right = []
    total = 0

    for line in input_data.splitlines():
        l, r = line.split()
        left_num = int(l)
        right_num = int(r)
        left.append(left_num)
        right.append(right_num)

    right_freq = Counter(right)

    for num in left:
        total += num * right_freq[num]

    return total


if __name__ == "__main__":
    input_data = open("input.txt").read().strip()
    print(f"Part 1: {part1(input_data)}")
    print(f"Part 2: {part2(input_data)}")
