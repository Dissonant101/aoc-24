def part1(input_data):
    total = 0
    grid = [list(row) for row in input_data.split("\n")]
    target_word = "XMAS"
    directions = [
        (0, 1),
        (0, -1),  # Horizontal
        (1, 0),
        (-1, 0),  # Vertical
        (1, 1),
        (-1, -1),  # Diagonal (main)
        (1, -1),
        (-1, 1),  # Diagonal (anti)
    ]

    for r in range(len(grid)):
        for c in range(len(grid[0])):
            for dr, dc in directions:
                current_sequence = []
                valid_path = True

                for i in range(len(target_word)):
                    nr, nc = r + i * dr, c + i * dc

                    if not (0 <= nr < len(grid) and 0 <= nc < len(grid[0])):
                        valid_path = False
                        break

                    current_sequence.append(grid[nr][nc])

                if valid_path and "".join(current_sequence) == target_word:
                    total += 1

    return total


def part2(input_data):
    total = 0
    grid = [list(row) for row in input_data.split("\n")]

    for r in range(1, len(grid) - 1):  # 'A' must be at least 1 unit from edge
        for c in range(1, len(grid[0]) - 1):  # 'A' must be at least 1 unit from edge
            # Check if the center character is 'A'
            if grid[r][c] == "A":
                diagonal_one = [grid[r - 1][c - 1], grid[r + 1][c + 1]]
                diagonal_two = [grid[r - 1][c + 1], grid[r + 1][c - 1]]

                if (
                    "M" in diagonal_one
                    and "S" in diagonal_one
                    and "M" in diagonal_two
                    and "S" in diagonal_two
                ):
                    total += 1

    return total


if __name__ == "__main__":
    input_data = open("input.txt").read().strip()
    print(f"Part 1: {part1(input_data)}")
    print(f"Part 2: {part2(input_data)}")
