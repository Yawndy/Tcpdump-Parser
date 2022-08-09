#!/usr/bin/python3
import file
import sys

file = open(sys.argv[1], "r")

all_lines = file.readalllines
print(all_lines)
file.close()
