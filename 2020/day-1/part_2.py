from pathlib import Path


def main() -> None:
    values = [int(value.rstrip()) for value in Path("day-1.in").open().readlines()]

    for value in values:
        sub_total = 2020 - value
        for inner_value in values:
            required_value = sub_total - inner_value
            if required_value in values:
                print(value * inner_value * required_value)
                return


if __name__ == "__main__":
    main()
