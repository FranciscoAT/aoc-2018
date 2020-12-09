from typing import Iterable, List


PRELOAD_LENGTH = 25
INPUT_FILE = "day9.in"
ENCRYPTION_WEAKNESS = 507622668


def main() -> None:
    for buffer in ingest():
        index = 0
        summed_values = 0
        while summed_values < ENCRYPTION_WEAKNESS:
            summed_values += buffer[index]
            index += 1

        if summed_values == ENCRYPTION_WEAKNESS:
            contiguous_buffer = sorted(buffer[:index])
            print(contiguous_buffer[0] + contiguous_buffer[-1])
            break


def ingest() -> Iterable[List[int]]:
    all_ints = [int(x) for x in open(INPUT_FILE).readlines()]
    for index in range(len(all_ints)):
        yield all_ints[index:]


if __name__ == "__main__":
    main()
