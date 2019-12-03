#!/bin/bash

dir_name=2019/day-${1}

mkdir -p ${dir_name}/src
touch ${dir_name}/src/{part_1.py,part_2.py,day-${1}.in,part-1.out,part-2.out}
touch ${dir_name}/README.md
