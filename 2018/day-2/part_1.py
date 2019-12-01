import itertools
import sys

id_list = [''.join(sorted(x.rstrip())) for x in open(sys.argv[1]).readlines()]
twos = 0
threes = 0

for ids in id_list:
    counts = [len(''.join(g)) for k, g in itertools.groupby(ids)]
    if 2 in counts:
        twos += 1
    if 3 in counts:
        threes += 1

print(twos * threes)
