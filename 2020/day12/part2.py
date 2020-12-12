from math import cos, pi, sin
from typing import Iterable, List, Tuple

FILE_IN = "day12.in"


def main() -> None:
    ship_pos = [0, 0]
    relative_waypoint_pos = [10, 1]
    for action, value in ingest():
        if action == "F":
            ship_pos[0] += relative_waypoint_pos[0] * value
            ship_pos[1] += relative_waypoint_pos[1] * value
        elif action == "N":
            relative_waypoint_pos[1] += value
        elif action == "S":
            relative_waypoint_pos[1] -= value
        elif action == "W":
            relative_waypoint_pos[0] -= value
        elif action == "E":
            relative_waypoint_pos[0] += value
        elif action == "R":
            relative_waypoint_pos = rotate_point(relative_waypoint_pos, 360 - value)
        else:
            relative_waypoint_pos = rotate_point(relative_waypoint_pos, value)

    print(abs(ship_pos[0]) + abs(ship_pos[1]))


def rotate_point(point: List[int], theta: int) -> List[int]:
    theta_radians = theta * pi / 180
    x_rot = cos(theta_radians) * point[0] - sin(theta_radians) * point[1]
    y_rot = sin(theta_radians) * point[0] + cos(theta_radians) * point[1]
    return [int(round(x_rot)), int(round(y_rot))]


def ingest() -> Iterable[Tuple[str, int]]:
    for line in open(FILE_IN).readlines():
        yield line[0], int(line[1:])


if __name__ == "__main__":
    main()
