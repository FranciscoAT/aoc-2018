# [Day 3](./src)

### [Part one](./src/part_1.py)

Runtime: 0.32s

A step up from the previous two days but still not too bad today. Basically we are given a [path file](./day-3/day-3.in) which consists of a comma seperated list with values of the form "{U,D,L,R}{integer distance}" (ex. "R123"). We are given two lists one for each wire. The question then is find the closest interseciton to the origin using Manhattan Distance, where the itnersection is the intersection of the two wires. The solution I approached was to make a list of each (x,y) coordiante each wire had went through. Then to find the intersection points of each wire, iterate through those and return the closest one.

### [Part two](./src/part_2.py)

Runtime: 0.63s

For part two I didn't need to change any code at all. It just wanted a different definition of "closest". Where closest in part 1 was defined by the Manhattan Distance of the intersection point. Here it is defined as the sum of path distance to the point for each wire. So changing up that line where we define closest distance, add 2 due to the way `list.index()` works and we get the right answer.
