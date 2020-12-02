from pathlib import Path


def main() -> None:
    values = [int(value.rstrip()) for value in Path("day-1.in").open().readlines()]

    for value in values:
        required_value = 2020 - value
        if required_value in values:
            print(value * required_value)
            break


if __name__ == "__main__":
    main()
