from typing import Iterable, List, Tuple


PRELOAD_LENGTH = 25
INPUT_FILE = "day9.in"


def main() -> None:
    for buffer, next_int in ingest():
        found = False
        for buffer_int in buffer:
            looking_for = next_int - buffer_int
            if looking_for in buffer:
                found = True
                break
        if found is False:
            print(next_int)
            break


def ingest() -> Iterable[Tuple[List[int], int]]:
    all_ints = [int(x) for x in open(INPUT_FILE).readlines()]

    for index, next_int in enumerate(all_ints[PRELOAD_LENGTH:]):
        yield all_ints[index : PRELOAD_LENGTH + index], next_int


if __name__ == "__main__":
    main()
