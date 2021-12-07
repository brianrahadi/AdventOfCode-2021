## What do you get if you multiply your final horizontal position by your final depth?

f = open("day2-input.txt", "r")

horizontal = 0
depth = 0

for line in f:
    dir, val = line.split() ## splits line into direction (forward, down, up) and value
    val = int(val)
    
    if dir == 'forward':
        horizontal += val
    elif dir == "down":
        depth += val
    else:
        depth -= val

print(horizontal * depth)
    