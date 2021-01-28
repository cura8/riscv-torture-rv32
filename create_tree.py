#!/usr/bin/env python3

import re
import pathlib
from typing import Dict, Any

# convert a number in a string that represent
# https://stackoverflow.com/questions/2267362/how-to-convert-an-integer-to-a-string-in-any-base

max_files_per_directory = 20

def numberToBase(n, b):
    if n == 0:
        return [0]
    digits = []
    while n:
        digits.append(int(n % b))
        n //= b
    return digits[::-1]


s_dir  = pathlib.Path('./output/tmp_tests/')


s_files = list(s_dir.glob('*.S'))

all_indexes = []

all_files = dict()

for f in s_files:
    # look for the index in the file name
    # (torture uses always the same scheme to number the files)
    match = re.search("\d+",str(f))
    if match:
        idx = int(match.group(0))
        all_indexes.append(int(idx))
        all_files[idx] = { 'origin' : str(f)}
first_idx, last_idx  = (min(all_indexes), max(all_indexes))

# maximum level of directories
max_depth = len(numberToBase(last_idx,max_files_per_directory))

# for each file, we compute the destination path depending of its
# index

for idx in all_indexes:
    target = numberToBase(idx,max_files_per_directory)
    l_target = len(target)
    padding = max_depth - l_target
    # if number of subdirectory is smaller than the "max" one
    # we pad with 0
    if padding >0:
        target = [0]*(padding) + target
    all_files[idx].update({'destination':  target})


    
print(f"Found {len(s_files)} files")
print(f" {first_idx} {last_idx}")
print(f"Max depth = {max_depth}")
res = numberToBase(1,20)
print(f"result = {res}")

res = numberToBase(100001,20)
print(f"result = {res}")
