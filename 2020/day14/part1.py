import re
from typing import Iterable, List, Tuple

FILE_IN = "day14.in"


def main() -> None:
    memory = dict()
    for mask, memory_position, value in ingest():
        memory[memory_position] = get_masked_value(mask, value)

    print(sum(memory.values()))


def get_masked_value(mask: List[Tuple[int, str]], value: int) -> int:
    bin_value_r_list = list("{0:b}".format(value).zfill(36))[::-1]
    for right_index, mask_value in mask:
        bin_value_r_list[right_index] = mask_value

    return int("".join(bin_value_r_list[::-1]), 2)


def ingest() -> Iterable[Tuple[List[Tuple[int, str]], int, int]]:
    current_mask = []
    for line in open(FILE_IN).readlines():
        line = line.strip().split(" = ")
        if line[0] == "mask":
            current_mask = []
            mask = list(line[1])[::-1]
            for right_index, value in enumerate(mask):
                if value != "X":
                    current_mask.append((right_index, value))
        else:
            memory_position = int(re.search(r"mem\[(\d+)\]", line[0]).group(1))
            value = int(line[1])
            yield current_mask, memory_position, value


if __name__ == "__main__":
    main()
