# What is the sum of the risk levels of all low points on your heightmap?

file = [list(x) for x in open('day9-input.txt').read().strip().split()]
  
low_points = []

def lower_than_adj(arr, r, c):
  if r > 0 and arr[r-1][c] <= arr[r][c]:
    return False
  if c > 0 and arr[r][c-1] <= arr[r][c]:
    return False
  rs = arr.__len__() # row size
  cs = arr[0].__len__() # col size
  if r < rs - 1 and arr[r+1][c] <= arr[r][c]:
    return False
  if c < cs - 1 and arr[r][c+1] <= arr[r][c]:
    return False
  return True

for r in range(file.__len__()):
  for c in range(file[r].__len__()):
    if (lower_than_adj(file, r, c)):
      low_points.append(int(file[r][c]) + 1)



print(sum(low_points))