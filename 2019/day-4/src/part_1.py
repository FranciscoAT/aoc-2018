def main() -> None:
    with open("day-4.in", "r") as input_file:
        min_password, max_password = (int(x) for x in input_file.readline().split("-"))

    valid_password_count = 0
    for password in range(min_password, max_password):
        password = str(password)
        if password == ''.join(sorted(password)) and adjacent_exists(password):
            valid_password_count += 1

    print(valid_password_count)


def adjacent_exists(password: str) -> bool:
    doubles = ["11", "22", "33", "44", "55", "66", "77", "88", "99", "00"]
    return any(x in password for x in doubles)


if __name__ == "__main__":
    main()
