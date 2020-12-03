import math
from typing import List, Tuple

PATHS = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]


def main() -> None:
    hill_map = ingest()
    slope_bottom = len(hill_map) - 1

    positions = [[0, 0] for _ in range(len(PATHS))]
    hit_counts = [0 for _ in range(len(PATHS))]

    min_curr_y_pos = 0

    while min_curr_y_pos < slope_bottom:
        for index, position in enumerate(positions):
            pos_x, pos_y, hit = determine_hit_and_move(
                position[0], position[1], hill_map, PATHS[index]
            )
            hit_counts[index] += 1 if hit else 0
            positions[index] = [pos_x, pos_y]

        min_curr_y_pos += 1

    for index, position in enumerate(positions):
        pos_x, pos_y, hit = determine_hit_and_move(
            position[0], position[1], hill_map, PATHS[index]
        )
        hit_counts[index] += 1 if hit else 0
        positions[index] = [pos_x, pos_y]

    print(math.prod(hit_counts))


def ingest() -> List[str]:
    return [line.strip() for line in open("day3.in")]


def determine_hit_and_move(
    pos_x: int, pos_y: int, hill_map: List[str], movement: Tuple[int, int]
) -> Tuple[int, int, bool]:
    if pos_y >= len(hill_map):
        return pos_x, pos_y, False
    hit = hill_map[pos_y][pos_x] == "#"
    pos_y += movement[1]
    pos_x = (pos_x + movement[0]) % len(hill_map[0])

    return pos_x, pos_y, hit


if __name__ == "__main__":
    main()
