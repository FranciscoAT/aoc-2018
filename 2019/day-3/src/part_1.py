from typing import List, Tuple


def main() -> None:
    with open("day-3.in", "r") as wires_file:
        wire_a = create_wire_path(wires_file.readline())
        wire_b = create_wire_path(wires_file.readline())

    print(find_closest_distance(wire_a, wire_b))


def create_wire_path(wire_in: str) -> List[Tuple[int, int]]:
    path = []
    pos_x = 0
    pos_y = 0

    for instruction in wire_in.split(","):
        direction = instruction[0]
        distance = int(instruction[1:])

        for _ in range(distance):
            if direction == "R":
                pos_x += 1
            elif direction == "D":
                pos_y -= 1
            elif direction == "L":
                pos_x -= 1
            elif direction == "U":
                pos_y += 1
            else:
                raise Exception("Something is off")

            path.append(tuple((pos_x, pos_y)))

    return path


def find_closest_distance(
    wire_a: List[Tuple[int, int]], wire_b: List[Tuple[int, int]]
) -> int:

    intersection_points = set(wire_a).intersection(set(wire_b))
    closest_distance = -1
    closest_intersection = ()

    for intersection_point in intersection_points:
        distance = abs(intersection_point[0]) + abs(intersection_point[1])
        if distance < closest_distance or closest_distance == -1:
            closest_intersection = intersection_point
            closest_distance = distance

    print(closest_intersection)
    return closest_distance


if __name__ == "__main__":
    main()
