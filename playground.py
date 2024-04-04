"""
0 3 5 4 6 9 2 7 8
7 8 2 1 0 5 6 0 9
0 6 0 2 7 8 1 3 5
3 2 1 0 4 6 8 9 7
8 0 4 9 1 3 5 0 6
5 9 6 8 2 0 4 1 3
9 1 7 6 5 2 0 8 0
6 0 3 7 0 1 9 5 2
2 5 8 3 9 4 7 6 0
"""
rows = [set() for _ in range(9)]
columns = [set() for _ in range(9)]
blocks = [set() for _ in range(9)]
arr = [[0]*9 for _ in range(9)]
coords = []
for i in range(9):
    row = [*map(int, input().split())]
    for j in range(9):
        if row[j]==0: coords.append((i, j))
        arr[i][j] = row[j]
        rows[i].add(row[j])
        columns[j].add(row[j])
        blocks[(i//3)*3+j//3].add(row[j])

def f(i: int):
    global rows, columns, blocks, arr, coords
    x, y = coords[i]
    for j in range(1, 10):
        if j not in rows[x] and\
           j not in columns[y] and\
           j not in blocks[(x//3)*3+y//3]:
            arr[x][y] = j
            if i==len(coords)-1:
                print("\n".join([" ".join(map(str, i)) for i in arr]))
                exit(0)
            else:
                rows[x].add(j)
                columns[y].add(j)
                blocks[(x//3)*3+y//3].add(j)
                f(i+1)
                rows[x].remove(j)
                columns[y].remove(j)
                blocks[(x//3)*3+y//3].remove(j)
f(0)








        







