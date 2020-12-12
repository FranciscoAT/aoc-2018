from typing import Iterable, Tuple

FILE_IN = "day12.in"


def main() -> None:
    latitude_pos = 0
    longitude_pos = 0
    direction = 90
    for action, value in ingest():
        if action == "F":
            if direction == 90:
                longitude_pos += value
            elif direction == 180:
                latitude_pos -= value
            elif direction == 270:
                longitude_pos -= value
            else:
                latitude_pos += value
        elif action == "N":
            latitude_pos += value
        elif action == "S":
            latitude_pos -= value
        elif action == "W":
            longitude_pos -= value
        elif action == "E":
            longitude_pos += value
        elif action == "R":
            direction = (direction + value) % 360
        else:
            direction = (direction - value) % 360

    print(abs(latitude_pos) + abs(longitude_pos))


def ingest() -> Iterable[Tuple[str, int]]:
    for line in open(FILE_IN).readlines():
        yield line[0], int(line[1:])


if __name__ == "__main__":
    main()
