from typing import List

FILE_IN = "day10.in"


def main() -> None:
    adapters = ingest()
    num_ways = {}
    num_ways[f"{adapters[-1] +3}"] = 1
    adapters.reverse()

    for adapter in adapters:
        ways = 0
        for i in range(1, 4):
            key = f"{adapter + i}"
            if key in num_ways:
                ways += num_ways[key]

        num_ways[f"{adapter}"] = ways

    print(num_ways['0'])


def ingest() -> List[int]:
    jolts = [int(x) for x in open(FILE_IN).readlines()]
    jolts.append(0)
    return sorted(jolts)


if __name__ == "__main__":
    main()
