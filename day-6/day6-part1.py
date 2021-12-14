## How many lanternfishes would there be after 80 days?

arr = [int(x) for x in open("day6-input.txt").read().strip().split(",")]

fishes = [arr.count(i) for i in range(9)]

for _ in range(80):
  num = fishes.pop(0)
  fishes[6] += num # add 6's
  fishes.append(num) # add 8's
      
print(sum(fishes))