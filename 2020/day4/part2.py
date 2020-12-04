from re import match
from typing import Dict, List

REQUIRED_FIELDS = set(["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"])


def main() -> None:
    count = 0
    for passport in ingest():
        count += 1 if validate(passport) is True else 0

    print(count)


def validate(passport: Dict) -> bool:
    if set(passport.keys()) != REQUIRED_FIELDS:
        return False

    if not (1920 <= int(passport["byr"]) <= 2002):
        return False

    if not (2010 <= int(passport["iyr"]) <= 2020):
        return False

    if not (2020 <= int(passport["eyr"]) <= 2030):
        return False

    height_unit = passport["hgt"][-2:]
    height = int(passport["hgt"][:-2])

    if height_unit == "in" and not (59 <= int(height) <= 76):
        return False
    if height_unit == "cm" and not (150 <= int(height) <= 193):
        return False

    if not match(r"^#[0-9a-f]{6}$", passport["hcl"]):
        return False

    if not match(r"^[0-9]{9}$", passport["pid"]):
        return False

    if passport["ecl"] not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
        return False

    return True


def ingest() -> List[Dict]:
    results = []
    lines = [line.strip() for line in open("day4.in").readlines()]
    passport = {}
    for line in lines:
        if line == "":
            results.append(passport)
            passport = {}
            continue
        for attribute in line.split(" "):
            attribute = attribute.split(":")
            if attribute[0] == "cid":
                continue
            passport[attribute[0]] = attribute[1]
    return results


if __name__ == "__main__":
    main()
