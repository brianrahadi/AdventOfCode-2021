# How much fuel must they spend to align to that position?

arr = [int(x) for x in open("day7-input.txt").read().strip().split(',')]

sum_dist = 0
min_sum_dist = 0

# i found min to be 0 and max to be 1935
for end_point in range(1935):
  for num in arr:
    sum_dist += abs(end_point - num)

  if min_sum_dist == 0:
    min_sum_dist = sum_dist
  elif sum_dist < min_sum_dist:
    min_sum_dist = sum_dist

  sum_dist = 0

print(min_sum_dist)
    
