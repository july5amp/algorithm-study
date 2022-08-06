import sys
sys.setrecursionlimit(10**4)

n = int(input())
map = [list(input()) for _ in range(n)]
cnt = 0
cnt2 = 0
visited = [[0 for col in range(n)] for row in range(n)]
visited2 = [[0 for col in range(n)] for row in range(n)]

def dfs(map, x, y, color):
    if x < 0 or x > n - 1 or y < 0 or y > n - 1:
        return False
    if map[x][y] == color:
        if visited[x][y] == 0:
            visited[x][y] = 1
            dfs(map, x - 1, y, color)
            dfs(map, x, y - 1, color)
            dfs(map, x + 1, y, color)
            dfs(map, x, y + 1, color)
            return True
def dfs2(map, x, y, color):
    if x < 0 or x > n - 1 or y < 0 or y > n - 1:
        return False
    if color == 'R':
        color = 'G'
    if map[x][y] == 'R':
        map[x][y] = 'G'
    if map[x][y] == color:
        if visited2[x][y] == 0:
            visited2[x][y] = 1
            dfs2(map, x - 1, y, color)
            dfs2(map, x, y - 1, color)
            dfs2(map, x + 1, y, color)
            dfs2(map, x, y + 1, color)
            return True

for x in range(n):
    for y in range(n):
        if dfs(map, x, y, map[x][y]):
            cnt = cnt + 1
for x in range(n):
    for y in range(n):
        if dfs2(map, x, y, map[x][y]):
            cnt2 = cnt2 + 1

print(cnt, cnt2)