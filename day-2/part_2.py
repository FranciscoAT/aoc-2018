import itertools
import sys

id_list = [x.rstrip() for x in open(sys.argv[1]).readlines()]
sliced_ids = []

for i in range(len(id_list[0])):
    sliced_ids = [(x[:i] + x[(i + 1):]) for x in id_list]
    if len(sliced_ids) > len(set(sliced_ids)):
        break

seen = []
id_1, id_2 = '', ''
for index, ids in enumerate(sliced_ids):
    if ids not in seen:
        seen.append(ids)
    else:
        id_1 = id_list[index]
        id_2 = id_list[seen.index(ids)]
        break

for i in range(len(id_1)):
    if id_1[i] != id_2[i]:
        print(id_1[:i] + id_1[(i + 1):])
        break