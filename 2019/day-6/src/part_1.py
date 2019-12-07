from typing import List


class Node:
    def __init__(self, name: str) -> None:
        self.name = name
        self.children = []

    def append_child(self, child_node: "Node") -> None:
        self.children.append(child_node)


def main() -> None:
    orbits = {}
    with open("day-6.in", "r") as orbit_file:
        alpha = set()
        beta = set()
        for orbit in orbit_file:
            orbit_definition = orbit.rstrip().split(")")
            if orbit_definition[0] not in orbits:
                orbits[orbit_definition[0]] = Node(orbit_definition[0])
            if orbit_definition[1] not in orbits:
                orbits[orbit_definition[1]] = Node(orbit_definition[1])

            alpha.add(orbit_definition[0])
            beta.add(orbit_definition[1])
            orbits[orbit_definition[0]].append_child(orbits[orbit_definition[1]])

    differences = alpha.difference(beta)
    if len(differences) != 1:
        raise Exception(f"something went wrong difference > 1: {differences}")

    print(get_orbit_count(orbits[differences.pop()], 0))


def get_orbit_count(node: Node, depth: int) -> int:
    orbit_count = 0
    for orbit in node.children:
        orbit_count += get_orbit_count(orbit, depth + 1)
    return orbit_count + depth


if __name__ == "__main__":
    main()
