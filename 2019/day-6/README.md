# [Day 6](./src)

### [Part one](./src/part_1.py)

Runtime: 0.03s

We got ourselves a Tree problem!! For part one we need to find what he called the number of orbits and intermediate orbits exist. For example:

```
          / -- D -- E
A -- B -- C -- F
```

would result in a total number of orbits + intermediate orbits of 13. As we cout `B --> A` = 1, `C --> A` = 2, `F --> A` = 3, `D --> A` = 3, `E --> A ` = 4. However a key to this solution is that this is simply the sum of the depth of each node. Where root node has a depth of 0. So the solution was to just start by constructing the tree. Then doing an easy DFS counting up the sum of the nodes.

### [Part two](./src/part_2.py)

Runtime: 0.03s

The second part also using the same tree from part one instead involves trying to find the shortest distance from Node "YOU" to Node "SAN". My solution here was to just construct the tree. Then to iterate from the "SAN" node all the way up to the root node setting the distance from the Node to the "SAN" node. Then repeat this for the "YOU" node however if we hit a node where the value for distance from "SAN" is not 0 we know that this node is a lowest parent node that has nodes "SAN" and "YOU" as some level of grand-children. Then we add up this nodes distance from "SAN" value and distance from "YOU" value and reduce that by 1 since we it's a shared node and we get the shortest path between "SAN" and "YOU".
