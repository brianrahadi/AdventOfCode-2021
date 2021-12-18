# At how many points do at least two lines overlap? (all type of lines)
file = [x for x in open("day5-input.txt").read().strip().split('\n')]

set = {}

for line in file:
  line = line.split(' -> ')
  line[0] = line[0].split(',')
  line[1] = line[1].split(',')

  x1, y1 = int(line[0][0]), int(line[0][1])
  x2, y2 = int(line[1][0]), int(line[1][1])

  if x1 == x2:
    x = x1
    ymin = y1 if y1 < y2 else y2
    ymax = y2 if y1 < y2 else y1

    for y in range(ymin, ymax+1):
      if (x, y) not in set:
        set[(x, y)] = 1
      else:
        set[(x, y)] += 1
  elif y1 == y2:
    y = y1
    xmin = x1 if x1 < x2 else x2
    xmax = x2 if x1 < x2 else x1

    for x in range(xmin, xmax+1):
      if (x, y) not in set:
        set[(x, y)] = 1
      else:
        set[(x, y)] += 1
  else:
    xmin = x1 if x1 < x2 else x2
    xmax = x2 if x1 < x2 else x1
    ystart = y1 if x1 < x2 else y2
    yend = y2 if x1 < x2 else y1
    inc = 0

    for x in range(xmin, xmax+1):
      if (x, ystart+inc) not in set:
        set[(x, ystart+inc)] = 1
      else:
        set[(x, ystart+inc)] += 1
      inc += 1 if ystart < yend else -1

    
counter = 0
for key in set:
  if set[key] > 1:
    counter += 1
print(counter)
