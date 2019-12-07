from typing import List


class Node:
    def __init__(self, name: str) -> None:
        self.name = name
        self.children = []
        self.parent = None
        self.santa_parent_count = 0
        self.you_parent_count = 0

    def append_child(self, child_node: "Node") -> None:
        self.children.append(child_node)


def main() -> None:
    orbits = {}
    santa_node = None
    you_node = None
    with open("day-6.in", "r") as orbit_file:
        for orbit in orbit_file:
            orbit_definition = orbit.rstrip().split(")")
            if orbit_definition[0] not in orbits:
                orbits[orbit_definition[0]] = Node(orbit_definition[0])
            if orbit_definition[1] not in orbits:
                orbits[orbit_definition[1]] = Node(orbit_definition[1])

            if orbit_definition[1] == "SAN":
                santa_node = orbits[orbit_definition[1]]
            if orbit_definition[1] == "YOU":
                you_node = orbits[orbit_definition[1]]

            orbits[orbit_definition[0]].append_child(orbits[orbit_definition[1]])
            orbits[orbit_definition[1]].parent = orbits[orbit_definition[0]]

    santa_parent_count = 0
    santa_parent = santa_node.parent
    while santa_parent is not None:
        santa_parent_count += 1
        santa_parent.santa_parent_count = santa_parent_count
        santa_parent = santa_parent.parent

    you_parent_count = 0
    you_parent = you_node.parent
    while you_parent is not None:
        you_parent_count += 1
        you_parent = you_parent.parent
        you_parent.you_parent_count = you_parent_count

        if you_parent.santa_parent_count != 0:
            print(you_parent.santa_parent_count + you_parent.you_parent_count - 1)
            break


if __name__ == "__main__":
    main()
