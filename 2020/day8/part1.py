from typing import List, Tuple


def main() -> None:
    executed_indexes = set()
    operations = ingest()

    accumulator = 0
    index = 0

    while True:
        if index in executed_indexes:
            break
        executed_indexes.add(index)
        instruction, value = operations[index]

        if instruction == "acc":
            accumulator += value
            index += 1
        elif instruction == "jmp":
            index += value
        elif instruction == "nop":
            index += 1

    print(accumulator)


def ingest() -> List[Tuple[str, int]]:
    operations = []
    for line in open("day8.in").readlines():
        line = line.rstrip().split(" ")
        operations.append((line[0], int(line[1])))

    return operations


if __name__ == "__main__":
    main()
