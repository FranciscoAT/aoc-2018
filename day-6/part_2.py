import sys

points = [list(map(int, x.split(','))) + [0] for x in open(sys.argv[1]).readlines()]

max_x = max(points, key=lambda x:x[0])[0]
max_y = max(points, key=lambda x:x[1])[1]

region_size = 0
for x in range(max_x + 1):
    for y in range(max_y + 1):
        total_dist = 0
        for point in points:
            total_dist += abs(x - point[0]) + abs(y - point[1])
        if total_dist < 10000:
            region_size += 1

print(region_size)
