#!/bin/bash

if [ -z $1 ]; then
    echo "Give a day number"
    exit 1
fi


DATE=2020/day${1}

git checkout -b ${DATE}
mkdir -p ${DATE}
touch ${DATE}/{part1.py,part2.py,day${1}.in}
cd ${DATE}
