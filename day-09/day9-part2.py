# What do you get if you multiply together the sizes of the three largest basins?

# I copied this answer from reddit, in here, I managed to learn about queue using python
from collections import deque

G = []

for line in open('day9-input.txt'):
    G.append([int(x) for x in list(line.strip())])

rs = len(G)
cs = len(G[0])

DR = [-1, 0, 1, 0]
DC = [0, 1, 0, -1]

ans = 0

S = []
SEEN = set()

for r in range(rs):
    for c in range(cs):
        if (r, c) not in SEEN and G[r][c] != 9:
            size = 0
            Q = deque()
            Q.append((r, c))
            while Q:
                (r, c) = Q.popleft()
                if (r, c) in SEEN:
                    continue
                SEEN.add((r, c))
                size += 1
                for d in range(4):
                    rr = r+DR[d]
                    cc = c+DC[d]
                    if 0 <= rr < rs and 0 <= cc < cs and G[rr][cc] != 9:
                        Q.append((rr, cc))
            S.append(size)
S.sort()
print(S[-1]*S[-2]*S[-3])