from pathlib import Path
from typing import Iterable, NamedTuple


class Password(NamedTuple):
    password: str
    character: str
    first_index: int
    second_index: int


def main() -> None:
    valid_count = 0
    for password in ingest():
        valid_count += 1 if asses_password(password) else 0

    print(valid_count)


def asses_password(password: Password) -> bool:
    first_character = password.password[password.first_index - 1]
    second_character = password.password[password.second_index - 1]
    return (first_character != second_character) and (
        first_character == password.character or second_character == password.character
    )


def ingest() -> Iterable[Password]:
    with Path("day2.in").open() as f:
        for password in f:
            password_list = password.rstrip().split(" ")
            min, max = password_list[0].split("-")
            first_index = int(min)
            second_index = int(max)
            character = password_list[1][:-1]
            password = password_list[-1]
            yield Password(
                password=password,
                character=character,
                first_index=first_index,
                second_index=second_index,
            )


if __name__ == "__main__":
    main()
