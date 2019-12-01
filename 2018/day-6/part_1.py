import sys

points = [list(map(int, x.split(','))) + [0] for x in open(sys.argv[1]).readlines()]

max_x = max(points, key=lambda x:x[0])[0]
max_y = max(points, key=lambda x:x[1])[1]

for x in range(max_x + 1):
    for y in range(max_y + 1):
        dist = 1000
        tie = False
        closest = None
        for index, point in enumerate(points):
            new_dist = abs(point[0] - x) + abs(point[1] - y)
            if new_dist < dist:
                dist = new_dist
                tie = False
                closest = index
            elif new_dist == dist:
                tie = True

        if points[closest][2] != -1:
            if (x == 0 or y == 0 or y == max_y or x == max_x) and tie is False:
                points[closest][2] = -1
            elif tie is False:
                points[closest][2] += 1

print(max(points, key=lambda x:x[2])[2])
