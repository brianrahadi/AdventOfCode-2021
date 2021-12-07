## What is the power consumption of the submarine? (Be sure to represent your answer in decimal, not binary.)

list = [x for x in open('day3-input.txt').read().strip().split("\n")]

len = list[0].__len__()

nums = [0] * len
i = 0

for i in range(list.__len__()):
    for j in range(len):
        nums[j] = nums[j] + 1 if list[i][j] == "1" else nums[j] - 1

gamma, epsilon = 0, 0
pos = len - 1

for num in nums:
    if num > 0:
        gamma += 2 ** pos
    else:
        epsilon += 2 ** pos
    pos -= 1

print(gamma * epsilon)
