## How many sums are larger than the previous sum?

import sys;

f = open("day1-input.txt", "r")
prev = sys.maxsize

counter = 0
size = 0
que = []

for x in f:
    num = int(x)
    if size < 3:
        que.append(num)
        size += 1
    else:
        prev = que.pop(0)
        if num > prev:
            counter += 1
        que.append(num)

print(counter)
        