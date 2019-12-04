#!/bin/bash

dir_name=2019/day-${1}

mkdir -p ${dir_name}/src
touch ${dir_name}/src/{part_1.py,part_2.py,day-${1}.in,part-1.out,part-2.out}
touch ${dir_name}/README.md

echo "- [Day ${1}](./day-${1})" >> ./2019/README.md
echo "# [Day ${1}](./src)" >> ./2019/day-${1}/README.md
echo "### [Part one](./src/part_1.py)" >> ./2019/day-${1}/README.md
echo "Runtime: xxx" >> ./2019/day-${1}/README.md
echo "### [Part two](./src/part_2.py)" >> ./2019/day-${1}/README.md
echo "Runtime: xxx" >> ./2019/day-${1}/README.md
