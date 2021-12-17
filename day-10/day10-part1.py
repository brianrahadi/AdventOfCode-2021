# What is the total syntax error score for those errors?
from collections import deque

file = [x for x in open('day10-input.txt').read().strip().split()]
# ): 3 points.
# ]: 57 points.
# }: 1197 points.
# >: 25137 points.

counter = {')': 0, ']': 0, '}': 0, '>': 0}
pair = {')':'(', ']': '[', '}': '{', '>': '<'}

stack = deque()

print(file[0])
for line in file:
  for char in line:
    if char not in counter:
      stack.appendleft(char)
    elif stack.popleft() != pair[char]:
      counter[char] += 1

def sumPoints(counter):
  sum = 0
  sum += counter[')'] * 3
  sum += counter[']'] * 57
  sum += counter['}'] * 1197
  sum += counter['>'] * 25137 
  return sum

print(sumPoints(counter))