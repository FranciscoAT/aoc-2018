import math


def main() -> None:
    total = 0

    with open("day-1.in", "r") as in_file:
        for module_num in in_file:
            total += int(math.floor(int(module_num) / 3.0) - 2)

    print(total)


if __name__ == "__main__":
    main()
