from typing import Iterable, List, Set


def main() -> None:
    sums = sum(len(set.intersection(*x)) for x in ingest())
    print(sums)


def ingest() -> Iterable[List[Set]]:
    answers_for_group = []
    for line in open("day6.in").readlines():
        line = line.rstrip()
        if not line:
            yield answers_for_group
            answers_for_group = []
            continue

        answers_for_group.append(set(list(line)))

    yield answers_for_group


if __name__ == "__main__":
    main()
