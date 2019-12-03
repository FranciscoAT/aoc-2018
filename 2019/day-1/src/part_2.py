import math


def main() -> None:
    total = 0

    with open("day-1.in", "r") as in_file:
        for module_num in in_file:
            total += get_fuel(int(module_num))

    print(total)


def get_fuel(fuel_in: int) -> int:
    required_fuel = int(math.floor(fuel_in / 3.0) - 2)

    if required_fuel <= 0:
        return 0

    return required_fuel + get_fuel(required_fuel)


if __name__ == "__main__":
    main()
