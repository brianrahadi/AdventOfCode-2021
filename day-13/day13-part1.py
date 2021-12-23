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

item = arr[0].split('=')

if item[0] == 'x':
  point = int(item[1])
  for coord in list(set):
    if coord[0] > point:
      new_coord = point * 2 - coord[0]
      set[(new_coord, coord[1])] = True
  max_x = point - 1
else:
  point = int(item[1])
  for coord in list(set):
    if coord[1] > point:
      new_coord = point * 2 - coord[1]
      set[(coord[0], new_coord)] = True
  max_y = point - 1

count = 0

for point in set:
  if (point[0] <= max_x and point[1] <= max_y):
    count += 1

print(count)

