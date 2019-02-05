#!/bin/bash

DAY_DIR=day-${1}
TEMPLATE=template.py

if [ -d ${DAY_DIR} ]; then
    echo "${DAY_DIR} already exists!"
else
    mkdir ${DAY_DIR} 
    cp ${TEMPLATE} ${DAY_DIR}/part_1.py
    cp ${TEMPLATE} ${DAY_DIR}/part_2.py
    touch ${DAY_DIR}/day_${1}.in
fi

cd ${DAY_DIR}
