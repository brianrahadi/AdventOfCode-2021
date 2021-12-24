# What do you get if you take the quantity of the most common element and subtract the quantity of the least common element? (40 steps)

# I realized my part 1 solution is very slow, so I searched and I realized i can use two counter dicts. https://www.reddit.com/r/adventofcode/comments/rfzq6f/comment/hohc8vc/?utm_source=reddit&utm_medium=web2x&context=3

# I learned about mapping and the *rules assignment from today's AOC :D.

from collections import Counter

poly, _, *rules = open('day14-input.txt').read().strip().split('\n')
rules = dict(r.split(" -> ") for r in rules)

pairs = Counter(map(str.__add__, poly, poly[1:]))
chars = Counter(poly)

for _ in range(40):
    for (a,b), c in pairs.copy().items():
        x = rules[a+b]
        pairs[a+b] -= c
        pairs[a+x] += c
        pairs[x+b] += c
        chars[x] += c

print(max(chars.values())-min(chars.values()))