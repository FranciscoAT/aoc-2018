from typing import List


def main() -> None:
    hill_map = ingest()
    slope_bottom = len(hill_map) - 1
    map_width = len(hill_map[0])
    pos_x, pos_y = 0, 0
    hit_count = 0

    while pos_y < slope_bottom:
        if hill_map[pos_y][pos_x] == "#":
            hit_count += 1

        pos_y += 1
        pos_x = (pos_x + 3) % map_width

    if hill_map[pos_y][pos_x] == "#":
        hit_count += 1

    print(hit_count)


def ingest() -> List[str]:
    return [line.strip() for line in open("day3.in")]


if __name__ == "__main__":
    main()
