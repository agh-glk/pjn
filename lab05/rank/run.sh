#!/bin/bash

TEST_FILE=../test.txt
APP=../lab4.py

cat $TEST_FILE | cut -f1 -d',' | $APP
