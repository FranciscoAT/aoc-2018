from copy import deepcopy
from typing import List, Tuple

FILE_IN = "day11.in"


STEPS = [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]


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

    num_in_sight = 0
    for step in STEPS:
        if check_in_step(grid, step, position, max_x, max_y):
            num_in_sight += 1

    if grid[target_y][target_x] == "L":
        return num_in_sight == 0
    else:
        return num_in_sight >= 5


def check_in_step(
    grid: List[List[str]],
    step: Tuple[int, int],
    position: Tuple[int, int],
    max_x: int,
    max_y: int,
) -> bool:
    step_x, step_y = step
    x, y = position
    while True:
        x += step_x
        y += step_y

        if x < 0 or x > max_x or y < 0 or y > max_y:
            return False

        if grid[y][x] == "#":
            return True
        elif grid[y][x] == "L":
            return False


def ingest() -> List[List[str]]:
    return [list(x.rstrip()) for x in open(FILE_IN).readlines()]


if __name__ == "__main__":
    main()
