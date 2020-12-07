from dataclasses import dataclass
import re
from typing import Iterable, List, Set, Tuple


@dataclass
class Node:
    value: str
    contained_in: Set["Node"]

    def __hash__(self) -> int:
        return hash(self.value)


def main() -> None:
    bags_dict = {}
    for bag_name, contains in ingest():
        bag_node = bags_dict.get(bag_name)
        if bag_node is None:
            bag_node = Node(value=bag_name, contained_in=set())
            bags_dict[bag_name] = bag_node

        for _, contained_bag_name in contains:
            contained_node = bags_dict.get(contained_bag_name)
            if contained_node is None:
                contained_node = Node(value=contained_bag_name, contained_in=set())
                bags_dict[contained_bag_name] = contained_node

            contained_node.contained_in.add(bag_node)

    golden_bag_node = bags_dict["shiny gold"]
    print(len(traverse(golden_bag_node, set())))


def traverse(current_node: Node, contained_bag_names: Set[str]) -> Set[str]:
    for bag_node in current_node.contained_in:
        if bag_node.value in contained_bag_names:
            continue
        contained_bag_names.add(bag_node.value)
        contained_bag_names = traverse(bag_node, contained_bag_names)

    return contained_bag_names


def ingest() -> Iterable[Tuple[str, List[Tuple[int, str]]]]:
    for line in open("day7.in").readlines():
        line = line.rstrip().split(" bags contain ")
        bag_name = line[0]
        contains = []
        for bag in line[1].split(", "):
            if "no other bags" in bag:
                break
            search = re.search(r"^(\d+)\ (.+)\ bag(s)?(.)?$", bag)
            contains.append((int(search.group(1)), search.group(2)))

        yield bag_name, contains


if __name__ == "__main__":
    main()
