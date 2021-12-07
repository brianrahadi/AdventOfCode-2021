## How many measurements are larger than the previous measurement?

import sys;

f = open("input.txt", "r")
prev = sys.maxsize
counter = 0

for x in f:
    num = int(x)   
    if num > prev:
        counter += 1
    prev = num

print(counter)