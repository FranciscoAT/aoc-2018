from typing import Iterable, Tuple


def main() -> None:
    generated_seat_ids = []
    for boarding_pass in ingest():
        row, column = get_row_column(boarding_pass)
        seat_id = row * 8 + column
        generated_seat_ids.append(seat_id)

    generated_seat_ids = sorted(generated_seat_ids)
    for index in range(1, len(generated_seat_ids) - 1):
        if generated_seat_ids[index] + 1 != generated_seat_ids[index + 1]:
            print(generated_seat_ids[index] + 1)


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
