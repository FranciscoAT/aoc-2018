from typing import List, Optional, Set, Tuple


def main() -> None:
    operations = ingest()

    for index in range(len(operations)):
        new_operations = operations[:]
        instruction, value = new_operations[index]
        if instruction in ["nop", "jmp"]:
            if instruction == "nop":
                new_operations[index] = ("jmp", value)
            else:
                new_operations[index] = ("nop", value)

            path_attempt = attempt_path(new_operations)
            if path_attempt:
                print(path_attempt)
                break


def attempt_path(
    operations: List[Tuple[str, int]],
) -> Optional[int]:
    accumulator = 0
    executed_indexes = set()
    index = 0
    while True:
        if index in executed_indexes:
            return None

        if index >= len(operations):
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

    return accumulator


def ingest() -> List[Tuple[str, int]]:
    operations = []
    for line in open("day8.in").readlines():
        line = line.rstrip().split(" ")
        operations.append((line[0], int(line[1])))

    return operations


if __name__ == "__main__":
    main()
