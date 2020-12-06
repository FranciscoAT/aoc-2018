from typing import Iterable, Set


def main() -> None:
    sums = sum(len(x) for x in ingest())
    print(sums)


def ingest() -> Iterable[Set]:
    answers_for_group = set()
    for line in open("day6.in").readlines():
        line = line.rstrip()
        if not line:
            yield answers_for_group
            answers_for_group = set()

        answers_for_group.update(list(line))

    yield answers_for_group

if __name__ == "__main__":
    main()
