## I am glad I am able to solve this problem.

## I completely solved this problem by myself though I took a lot of time and searched for some function docs.

file = [x for x in open('day13-input.txt').read().strip().split('\n')]

set = {}

arr = []

max_x = 0
max_y = 0
for line in file:
  if line and line.startswith('fold'):
    arr.append(line.split()[-1])
  elif line:
    x, y = line.split(',')
    x, y = int(x), int(y)
    max_x = x if x > max_x else max_x
    max_y = y if y > max_y else max_y
    set[(x, y)] = True

for i in range(arr.__len__()):
  item = arr[i].split('=')
  if item[0] == 'x':
    point = int(item[1])
    for coord in list(set):
      if coord[0] > point and coord[0] <= max_x:
        new_coord = point * 2 - coord[0]
        set[(new_coord, coord[1])] = True
    max_x = point - 1
  elif item[0] == 'y':
    point = int(item[1])
    for coord in list(set):
      if coord[1] > point and coord[1] <= max_y:
        new_coord = point * 2 - coord[1]
        set[(coord[0], new_coord)] = True
    max_y = point - 1

answer = ''

for y in range(max_y + 1):
  for x in range(max_x + 1):
    answer += 'X' if (x,y) in set else ' '
  answer += '\n'

print(answer)