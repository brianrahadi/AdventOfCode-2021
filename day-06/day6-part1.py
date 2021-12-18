## How many lanternfishes would there be after 80 days?

# I initially made a 2d array and made all the changes until I realized I can just make a 9-sized queue. Code cited from https://www.reddit.com/r/adventofcode/comments/r9z49j/2021_day_6_solutions/hnfaisu/?utm_source=reddit&utm_medium=web2x&context=3

arr = [int(x) for x in open("day6-input.txt").read().strip().split(",")]

fishes = [arr.count(i) for i in range(9)]

for _ in range(80):
  num = fishes.pop(0)
  fishes[6] += num # add 6's
  fishes.append(num) # add 8's
      
print(sum(fishes))