## What is the life support rating of the submarine? (Be sure to represent your answer in decimal, not binary.)

## I was stuck, I learnt Counter and more about python from https://www.reddit.com/r/adventofcode/comments/r7r0ff/2021_day_3_solutions/hn17b24/?context=3

from collections import Counter

list = [x for x in open('day3-input.txt').read().strip().split('\n')]
list2 = list

gamma = ''
epsilon = ''


for i in range(len(list[0])):
    common = Counter([x[i] for x in list])
    if common['0'] > common['1']:
        list = [num for num in list if num[i] == '0']
    else:
        list = [num for num in list if num[i] == '1'] ## equal is 1
    if list:
        gamma = list[0]


for i in range(len(list2[0])):
    common = Counter([x[i] for x in list2])
    if common['0'] > common['1']:
        list2 = [num for num in list2 if num[i] == '1']
    else:
        list2 = [num for num in list2 if num[i] == '0'] ## equal is 0
    if list2:
        epsilon = list2[0]

print(int(gamma, 2) * int(epsilon, 2))