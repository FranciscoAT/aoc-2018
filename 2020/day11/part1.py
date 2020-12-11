from copy import deepcopy
from typing import List, Tuple

# FILE_IN = "test.in"
FILE_IN = "day11.in"


def main() -> None:
    previous_grid = []
    current_grid = ingest()

    max_y = len(current_grid) - 1
    max_x = len(current_grid[0]) - 1

    while True:
        if previous_grid == current_grid:
            break

        new_grid = deepcopy(current_grid)

        for y, row in enumerate(new_grid):
            for x, character in enumerate(row):
                if character == ".":
                    continue

                should_change = change_state(current_grid, (x, y), max_x, max_y)
                if should_change:
                    if character == "L":
                        new_grid[y][x] = "#"
                    else:
                        new_grid[y][x] = "L"

        previous_grid = current_grid
        current_grid = new_grid

    occupied_seats = 0
    for row in current_grid:
        occupied_seats += row.count("#")

    print(occupied_seats)


def change_state(
    grid: List[List[str]], position: Tuple[int, int], max_x: int, max_y: int
) -> bool:
    target_x, target_y = position
    positions = [
        (target_x - 1, target_y - 1),
        (target_x, target_y - 1),
        (target_x + 1, target_y - 1),
        (target_x - 1, target_y),
        (target_x + 1, target_y),
        (target_x - 1, target_y + 1),
        (target_x, target_y + 1),
        (target_x + 1, target_y + 1),
    ]

    num_occupied_adjacent = 0
    for x, y in positions:
        if x < 0 or x > max_x or y < 0 or y > max_y:
            continue

        if grid[y][x] == "#":
            num_occupied_adjacent += 1

    if grid[target_y][target_x] == "L":
        return num_occupied_adjacent == 0
    else:
        return num_occupied_adjacent >= 4


def ingest() -> List[List[str]]:
    return [list(x.rstrip()) for x in open(FILE_IN).readlines()]


if __name__ == "__main__":
    main()
