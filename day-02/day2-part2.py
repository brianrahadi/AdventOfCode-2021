## What do you get if you multiply your final horizontal position by your final depth?

f = open("day2-input.txt", "r")

aim = 0
horizontal = 0
depth = 0

for line in f:
    dir, val = line.split()
    val = int(val)
    if dir == 'forward':
        horizontal += val
        depth += val * aim
    elif dir == "down":
        aim += val
    else:
        aim -= val

print(horizontal * depth)