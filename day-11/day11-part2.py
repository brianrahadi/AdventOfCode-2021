# What is the first step during which all octopuses flash?

file = [x for x in open('day11-input.txt').read().strip().split()]

def create_bool(rs, cs):
  bool_arr = []
  for i in range(rs):
    bool_arr.append([False] * cs)
  return bool_arr

def valid_index(i, j):
  if 0 <= i and i < rs and 0 <= j and j < cs:
    return True
  return False

def increment(i, j):
  if not valid_index(i, j) or arr[i][j] == 0:
    return
  arr[i][j] += 1 

def flash(i, j):
  if not valid_index(i, j):
    return
  if flashed[i][j]:
    return

  arr[i][j] += 1
  flashed[i][j] = True

  for r in [-1, 0, 1]:
    for c in [-1, 0, 1]:
      if (r == 0 and c == 0):
        continue
      increment(i + r, j + c)
      check_flash(i + r, j + c)

def check_flash(i, j):
  if not valid_index(i, j):
    return
  if arr[i][j] > 9 and not flashed[i][j]:
    # global total_flashes
    # total_flashes += 1
    flash(i, j) # flashed[i][j] = True
    arr[i][j] = 0

def printy(arr):
  for line in arr:
    print(line)

def start_flash():
  for i in range(rs):
    for j in range(cs):
      arr[i][j] += 1
  for i in range(rs):
    for j in range(cs):
      check_flash(i, j)

def all_flashed():
  for i in range(rs):
    for j in range(cs):
      if not flashed[i][j]:
        return False
  return True

# start
arr = []

for i in range(file.__len__()):
  sub_arr = []
  for char in file[i]:
    sub_arr.append(int(char))
  arr.append(sub_arr)

rs = arr.__len__()
cs = arr[0].__len__()

steps = 0

while True:
  steps += 1
  flashed = create_bool(rs, cs)
  start_flash()
  if all_flashed():
    break
  
print(steps)