import re
from typing import Iterable, List, Tuple

FILE_IN = "day14.in"


def main() -> None:
    memory = dict()
    for mask, memory_position, value in ingest():
        for mem_pos in get_memory_locations(memory_position, mask):
            memory[mem_pos] = value

    print(sum(memory.values()))


def get_memory_locations(
    memory_position: int, mask: List[Tuple[int, str]]
) -> List[int]:
    memory_position_r_list = list("{0:b}".format(memory_position).zfill(36))[::-1]
    for right_index, mask_value in mask:
        memory_position_r_list[right_index] = mask_value

    return [
        int("".join(x[::-1]), 2)
        for x in recurse_memeory_locations(memory_position_r_list)
    ]


def recurse_memeory_locations(memory_list: List[str]) -> List[List[str]]:
    if "X" not in memory_list:
        return [memory_list]

    x_index = memory_list.index("X")

    variation_0 = memory_list.copy()
    variation_0[x_index] = "0"
    variation_1 = memory_list.copy()
    variation_1[x_index] = "1"

    output = []
    for variation in [variation_0, variation_1]:
        output.extend(recurse_memeory_locations(variation))

    return output


def ingest() -> Iterable[Tuple[List[Tuple[int, str]], int, int]]:
    current_mask = []
    for line in open(FILE_IN).readlines():
        line = line.strip().split(" = ")
        if line[0] == "mask":
            current_mask = []
            mask = list(line[1])[::-1]
            for right_index, value in enumerate(mask):
                if value != "0":
                    current_mask.append((right_index, value))
        else:
            memory_position = int(re.search(r"mem\[(\d+)\]", line[0]).group(1))
            value = int(line[1])
            yield current_mask, memory_position, value


if __name__ == "__main__":
    main()
