import sys
sys.setrecursionlimit(10**4)

n = int(input())

rgb = [0 for _ in range(n)]
for i in range(n):
    rgb[i] = input()

visited_a = [[False]*n for _ in range(n)]
visited_b = [[False]*n for _ in range(n)]
count_a = 0
count_b = 0
color = ''

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def dfs_a(x, y, color):
    if x < 0 or x >= n or y < 0 or y >= n:
        return
    visited_a[x][y] = True
    for i in range(4):
        if x + dx[i] < 0 or x + dx[i] >= n or y + dy[i] < 0 or y + dy[i] >= n:
            continue
        if rgb[x + dx[i]][y + dy[i]] == color and not visited_a[x + dx[i]][y + dy[i]]:
            dfs_a(x + dx[i], y + dy[i], color)


def dfs_b(x, y, color):
    if x < 0 or x >= n or y < 0 or y >= n:
        return
    visited_b[x][y] = True
    for i in range(4):
        if x + dx[i] < 0 or x + dx[i] >= n or y + dy[i] < 0 or y + dy[i] >= n:
            continue
        if (rgb[x + dx[i]][y + dy[i]] == color or (rgb[x + dx[i]][y + dy[i]] != 'B' and color != 'B')) and not visited_b[x + dx[i]][y + dy[i]]:
            dfs_b(x + dx[i], y + dy[i], color)


for i in range(n):
    for j in range(n):
        if not visited_a[j][i]:
            dfs_a(j, i, rgb[j][i])
            count_a += 1
        if not visited_b[j][i]:
            dfs_b(j, i, rgb[j][i])
            count_b += 1

print(count_a, count_b)