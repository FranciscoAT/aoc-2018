from typing import List

FILE_IN = "day10.in"


def main() -> None:
    adapters = ingest()
    adapters.append(adapters[-1] + 3)
    jumps = [0, 0, 0]
    current_joltage = 0

    for adapter in adapters:
        jumps[adapter - current_joltage - 1] += 1
        current_joltage = adapter

    print(jumps[0] * jumps[2])


def ingest() -> List[int]:
    return sorted([int(x) for x in open(FILE_IN).readlines()])


if __name__ == "__main__":
    main()
