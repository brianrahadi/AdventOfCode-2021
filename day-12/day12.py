## Today has a really hard quiz for me. Even though I have learned graph algorithms in cpp, I need to develop more algorithmic thinking to solve more of these kind of problems.

## I learned about defaultdict from here, which is a data structure used for graphs

## Code from "https://www.reddit.com/r/adventofcode/comments/rehj2r/comment/ho7x83o/?utm_source=reddit&utm_medium=web2x&context=3"

from collections import defaultdict
neighbours = defaultdict(list)

for line in open('day12-input.txt'):
    a, b = line.strip().split('-')
    neighbours[a] += [b]
    neighbours[b] += [a]

def count(part, seen=[], cave='start'):
    if cave == 'end': return 1
    if cave in seen:
        if cave == 'start': return 0
        if cave.islower():
            if part == 1: return 0
            else: part = 1
    return sum(count(part, seen+[cave], n) for n in neighbours[cave])

print(count(part=1), count(part=2))