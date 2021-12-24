# What do you get if you take the quantity of the most common element and subtract the quantity of the least common element?

# Did it by myself, though not the most efficient :)

from collections import Counter

file = [x for x in open('day14-input.txt').read().strip().split('\n')]

answer = list(file[0])

set = {}

for i in range(2, file.__len__()):
  key, value = file[i].split(' -> ', 2)
  set[key] = value

steps = 10
size = answer.__len__()
i = 0

for _ in range(steps):
  while i < answer.__len__() - 1:
    char = answer[i] + answer[i+1]
    answer.insert(i+1, set[char])
    i += 2
  i = 0

c = Counter(answer)
print(c)
print(c.most_common()[0][1] - c.most_common()[-1][1])
# print(answer)