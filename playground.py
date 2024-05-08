"""
문제
N×M의 행렬로 표현되는 맵이 있다. 맵에서 0은 이동할 수 있는 곳을 나타내고, 1은 이동할 수 없는 벽이 있는 곳을 나타낸다. 
당신은 (1, 1)에서 (N, M)의 위치까지 이동하려 하는데, 이때 최단 경로로 이동하려 한다. 
최단경로는 맵에서 가장 적은 개수의 칸을 지나는 경로를 말하는데, 이때 시작하는 칸과 끝나는 칸도 포함해서 센다.

만약에 이동하는 도중에 한 개의 벽을 부수고 이동하는 것이 좀 더 경로가 짧아진다면, 
벽을 한 개 까지 부수고 이동하여도 된다.

한 칸에서 이동할 수 있는 칸은 상하좌우로 인접한 칸이다.

맵이 주어졌을 때, 최단 경로를 구해 내는 프로그램을 작성하시오.

입력
첫째 줄에 N(1 ≤ N ≤ 1,000), M(1 ≤ M ≤ 1,000)이 주어진다. 
다음 N개의 줄에 M개의 숫자로 맵이 주어진다. (1, 1)과 (N, M)은 항상 0이라고 가정하자.

출력
첫째 줄에 최단 거리를 출력한다. 불가능할 때는 -1을 출력한다.

예제 입력 1 
6 4
0100
1110
1000
0000
0111
0000
예제 출력 1 
15
예제 입력 2 
4 4
0111
1111
1111
1110
예제 출력 2 
-1
"""
from sys import stdin
from collections import deque
from copy import deepcopy

H, W = map(int, stdin.readline().split())
walls = []
MAP = [[0]*W for _ in range(H)]
for i in range(H):
    s = stdin.readline()
    for j in range(W):
        if int(s[j]):
            walls.append((i, j))
            MAP[i][j] = 1
hole = None
for i in range(H):
    for j in range(W):
        x = MAP[i][j]
        if not x:
            opened = False
            if (i>0 and MAP[i-1][j]==0) or \
               (j>0 and MAP[i][j-1]==0) or \
               (i<H-1 and MAP[i+1][j]==0) or \
               (j<W-1 and MAP[i][j+1]==0):
                opened = True
            if not opened:

                

MAPS = []
MAPS.append(deepcopy(MAP))
for i, j in walls:
    temp = deepcopy(MAP)
    temp[i][j] = 0
    MAPS.append(temp)
answer = None
for m in MAPS:
    q = deque([(1, 0, 0)])
    m[0][0] = 1
    while q:
        count, row, col = q.popleft()
        if row==H-1 and col==W-1:
            answer = count if answer is None else min(count, answer)
        count += 1
        if row>0 and m[row-1][col]==0:
            m[row-1][col] = 1
            q.append((count, row-1, col))
        if col>0 and m[row][col-1]==0:
            m[row][col-1] = 1
            q.append((count, row, col-1))
        if row<H-1 and m[row+1][col]==0:
            m[row+1][col] = 1
            q.append((count, row+1, col))
        if col<W-1 and m[row][col+1]==0:
            m[row][col+1] = 1
            q.append((count, row, col+1))
print(-1 if answer is None else answer)


