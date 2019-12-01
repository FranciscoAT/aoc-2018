sum = 0
with open('part_1.in', 'r') as f:
    for line in f:
        sum += int(line.rstrip())
print(sum)