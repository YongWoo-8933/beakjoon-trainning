"""
6 4
1 -1 0 0 0 0
0 -1 0 0 0 0
0 0 0 0 -1 0
0 0 0 0 -1 1
"""
from sys import stdin
import collections
W, H = map(int, stdin.readline().split())
# M = [[*map(int, i.split())] for i in stdin]
# M = [
#     [1, -1, 0, 0, 0, 0],
#     [0, -1, 0, 0, 0, 0],
#     [0, 0, 0, 0, -1, 0],
#     [0, 0, 0, 0, -1, 1],
# ]
# M = [
#     [0 ,-1, 0, 0, 0, 0],
#     [-1, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0,],
#     [0, 0, 0, 0, 0, 1,],
# ]
# M = [
#     [0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 1],
# ]
# M = [
#     [-1, 1, 0, 0, 0],
#     [0, -1, -1, -1, 0],
#     [0, -1, -1, -1, 0],
#     [0, -1, -1, -1, 0],
#     [0, 0, 0, 0, 0],
# ]
# M = [
#     [1, -1],
#     [-1, 1],
# ]
result = M
check = [[1]*W for _ in range(H)]
q = collections.deque()
for i in range(H):
    for j in range(W):
        m = M[i][j]
        if m == 1:
            q.append((0, i, j))
            check[i][j] = 0
        if m == -1:
            check[i][j] = 0

max_value = -1
while q:
    next_q = collections.deque()
    while q:
        value, row, col = q.popleft()
        x = M[row][col]

        if x==-1: 
            continue
        elif x==0:
            value += 1
        elif x==1 and check[row][col]:
            check[row][col] = 0
            q.append((value, row, col))

        max_value = max(max_value, value)

        if row > 0 and check[row-1][col]:
            check[row-1][col] = 0
            q.append((value, row-1, col))
        if row < H-1 and check[row+1][col]:
            check[row+1][col] = 0
            q.append((value, row+1, col))
        if col > 0 and check[row][col-1]:
            check[row][col-1] = 0
            q.append((value, row, col-1))
        if col < W-1 and check[row][col+1]:
            check[row][col+1] = 0
            q.append((value, row, col+1))

print(-1 if sum(sum(i) for i in check) else max_value)








