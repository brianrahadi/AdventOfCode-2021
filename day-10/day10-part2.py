# What is the middle score?
# might not be the most efficient, but really proud i can finish all day 10 by myself :)

from collections import deque

file = [x for x in open('day10-input.txt').read().strip().split()]

# [({(<(())[]>[[{[]{<()<>> - Complete by adding }}]])})].
# [(()[<>])]({[<{<<[]>>( - Complete by adding )}>]}).
# (((({<>}<{<{<>}{[]{[]{} - Complete by adding }}>}>)))).
# {<[[]]>}<{[{[{[]{()[[[] - Complete by adding ]]}}]}]}>.
# <{([{{}}[<[[[<>{}]]]>[]] - Complete by adding ])}>.

pair = {')':'(', ']': '[', '}': '{', '>': '<'}

def count_score(line):
  points = {'(': 1, '[': 2, '{': 3, '<': 4} # this should be it's closing, but still OK!
  sum = 0
  for char in line:
    sum *= 5
    sum += points[char]
  return sum

answer_points = []

for line in file:
  corrupted = False
  stack = deque()

  for char in line:
    if char not in pair:
      stack.appendleft(char)
    elif stack.popleft() != pair[char]:
      corrupted = True
      break
    
  if corrupted:
    continue

  answer = ''
  while stack:
    answer += stack.popleft()
  
  answer_points.append(count_score(answer))

answer_points.sort()

print(answer_points[answer_points.__len__() // 2])