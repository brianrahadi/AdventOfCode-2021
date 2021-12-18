## In the output values, how many times do digits 1, 4, 7, or 8 appear?

file = [x for x in open('day8-input.txt').read().strip().split('\n')]

for i in range(file.__len__()):
  file[i] = file[i].split('| ', 1)[1].split(' ')

## length -> digit
# 2 -> 1
# 3 -> 7
# 4 -> 4
# 7 -> 8
set = {}
set[1] = 0
set[4] = 0
set[7] = 0
set[8] = 0

for i in range(file.__len__()):
  for line in file[i]:
    length = line.__len__()
    if length == 2:
      set[1] += 1
    elif length == 3:
      set[7] += 1
    elif length == 4:
      set[4] += 1
    elif length == 7:
      set[8] += 1

counts = [set[x] for x in set]

print(sum(counts))
