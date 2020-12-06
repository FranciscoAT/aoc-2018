from typing import Iterable, Tuple


def main() -> None:
    max_seat_id = 0
    for boarding_pass in ingest():
        row, column = get_row_column(boarding_pass)
        seat_id = row * 8 + column
        if seat_id > max_seat_id:
            max_seat_id = seat_id

    print(max_seat_id)


def get_row_column(boarding_pass: str) -> Tuple[int, int]:
    row_range = [0, 127]
    column_range = [0, 8]

    for command in boarding_pass:
        if command == "F":
            row_range[-1] -= int((row_range[1] - row_range[0] + 1) / 2)
        elif command == "B":
            row_range[0] += int((row_range[1] - row_range[0] + 1) / 2)
        if command == "L":
            column_range[-1] -= int((column_range[1] - column_range[0] + 1) / 2)
        elif command == "R":
            column_range[0] += int((column_range[1] - column_range[0] + 1) / 2)

    return row_range[0], column_range[0]


def ingest() -> Iterable[str]:
    for line in open("day5.in").readlines():
        yield line.rstrip()


if __name__ == "__main__":
    main()
