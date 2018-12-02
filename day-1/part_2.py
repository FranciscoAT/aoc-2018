import sys

sum = 0
index = 0
seen = set()
num_list = []

with open(sys.argv[1], 'r') as nums:
    for num in nums:
        num_list.append(int(num.rstrip()))


while sum not in seen:
    seen.add(sum)
    sum += num_list[index % len(num_list)]
    index += 1

print(sum)