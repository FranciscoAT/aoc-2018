from dataclasses import dataclass
import re
from typing import Iterable, List, Tuple


@dataclass
class Node:
    value: str
    contains: List[Tuple[int, "Node"]]

    def __hash__(self) -> int:
        return hash(self.value)


def main() -> None:
    bags_dict = {}
    for bag_name, contains in ingest():
        bag_node = bags_dict.get(bag_name)
        if bag_node is None:
            bag_node = Node(value=bag_name, contains=[])
            bags_dict[bag_name] = bag_node

        for count, contained_bag_name in contains:
            contained_node = bags_dict.get(contained_bag_name)
            if contained_node is None:
                contained_node = Node(value=contained_bag_name, contains=[])
                bags_dict[contained_bag_name] = contained_node

            bag_node.contains.append((count, contained_node))

    golden_bag_node = bags_dict["shiny gold"]
    print(traverse(golden_bag_node))


def traverse(current_node: Node) -> int:
    count = 0
    for bag_count, bag_node in current_node.contains:
        count += bag_count + bag_count * traverse(bag_node)

    return count


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
