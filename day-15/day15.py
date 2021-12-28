import heapq
## Dijkstra's algorithm is indeed quite challenging for me ;). https://www.reddit.com/r/adventofcode/comments/rgqzt5/comment/holzpnj/?utm_source=reddit&utm_medium=web2x&context=3.
# I learned about heappop in this day 15 quiz.

G = [x for x in open('day15-input.txt').read().strip().split()]

R = G.__len__()
C = G[0].__len__()

for i in range(R):
  arr = [None] * C
  for j in range(C):
    arr[j] = int(G[i][j])
  G[i] = arr
  
DR = [-1,0,1,0]
DC = [0,1,0,-1]

def solve(n_tiles):
    D = [[None for _ in range(n_tiles*C)] for _ in range(n_tiles*R)]
    Q = [(0,0,0)]
    while Q:
        (dist,r,c) = heapq.heappop(Q)

        if r<0 or r>=n_tiles*R or c<0 or c>=n_tiles*C:
            continue

        val = G[r%R][c%C] + (r//R) + (c//C)

        if val > 9:
          val = val % 9

        rc_cost = dist + val

        if D[r][c] is None or rc_cost < D[r][c]:
            D[r][c] = rc_cost
        else:
            continue
        if r==n_tiles*R-1 and c==n_tiles*C-1:
            break

        for d in range(4):
            rr = r+DR[d]
            cc = c+DC[d]
            heapq.heappush(Q, (D[r][c],rr,cc))
    return D[n_tiles*R-1][n_tiles*C-1] - G[0][0]

print(solve(1))
print(solve(5))