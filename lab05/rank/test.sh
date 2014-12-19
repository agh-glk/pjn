#!/bin/bash

TEST_FILE=../test.txt
APP=../lab4.py

cat $TEST_FILE | cut -f1 -d',' > input.txt
$APP input.txt > output.txt
cat output.txt | python ./rank.py -n $TEST_FILE
rm input.txt output.txt
