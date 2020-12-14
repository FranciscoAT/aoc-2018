from typing import List, Tuple

FILE_IN = "day13.in"


def main() -> None:
    earliest_departure, busses = ingest()
    index = earliest_departure
    found_bus = None
    while True:
        for bus in busses:
            if (index % bus) == 0:
                found_bus = bus
                break
        if found_bus:
            break
        index += 1

    print((index - earliest_departure) * found_bus)


def ingest() -> Tuple[int, List[int]]:
    lines = [x.rstrip() for x in open(FILE_IN).readlines()]
    return int(lines[0]), [int(x) for x in lines[1].split(",") if x != "x"]


if __name__ == "__main__":
    main()
