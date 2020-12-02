from pathlib import Path
from typing import Any, Dict, Iterable


def main() -> None:
    valid_count = 0
    for password in ingest():
        valid_count += 1 if asses_password(password) else 0

    print(valid_count)


def asses_password(password: Dict) -> bool:
    char_count = password["password"].count(password["char"])
    return password["min"] <= char_count and password["max"] >= char_count


def ingest() -> Iterable[Dict[str, Any]]:
    with Path("day2.in").open() as f:
        for password in f:
            password_dict: Dict[str, Any] = {}
            password_list = password.rstrip().split(" ")
            min, max = password_list[0].split("-")
            password_dict["min"] = int(min)
            password_dict["max"] = int(max)
            password_dict["char"] = password_list[1][:-1]
            password_dict["password"] = password_list[-1]
            yield password_dict


if __name__ == "__main__":
    main()
