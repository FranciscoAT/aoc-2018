#!/bin/bash

YEAR=2020

dir_name=${YEAR}/day-${1}

mkdir -p ${dir_name}
touch ${dir_name}/{part_1.py,part_2.py,day-${1}.in}
