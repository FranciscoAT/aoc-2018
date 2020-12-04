from typing import List


def main() -> None:
    count = 0
    for passport in ingest():
        count += 1 if validate(passport) else 0

    print(count)


def validate(passport: str) -> bool:
    required_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    for field in required_fields:
        if field not in passport:
            return False
    return True


def ingest() -> List[str]:
    return [
        passport.replace("\n", "") for passport in open("day4.in").read().split("\n\n")
    ]


if __name__ == "__main__":
    main()
