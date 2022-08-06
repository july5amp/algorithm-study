import sys
sys.setrecursionlimit(10**4)

n = int(input())
grid = [list(input().strip()) for _ in range(n)]
visitA = [[0 for _ in range(n)] for _ in range(n)]
visitB = [[0 for _ in range(n)] for _ in range(n)]
cntA = 0
cntB = 0

def dfsA(x, y, color):
    if not (0 <= x <= n - 1 and 0 <= y <= n - 1):
        return False
    elif grid[x][y] == color:
        if visitA[x][y] == 0:
            visitA[x][y] = 1
            dfsA(x + 1, y, color)
            dfsA(x - 1, y, color)
            dfsA(x, y + 1, color)
            dfsA(x, y - 1, color)
            return True

def dfsB(x, y, color):
    if color=='R':  color='G'
    if not (0 <= x <= n - 1 and 0 <= y <= n - 1):
        return False
    if grid[x][y] == 'R':
        grid[x][y] = 'G'
    if grid[x][y] == color: # or (grid[x][y] != 'B' and color != 'B'):
        if visitB[x][y] == 0:
            visitB[x][y] = 1
            dfsB(x + 1, y, color)
            dfsB(x - 1, y, color)
            dfsB(x, y + 1, color)
            dfsB(x, y - 1, color)
            return True

for i in range(n):
    for k in range(n):
        if dfsA(i, k, grid[i][k]):
            cntA += 1
for i in range(n):
    for k in range(n):
        if dfsB(i, k, grid[i][k]):
            cntB += 1

print(cntA, cntB)
