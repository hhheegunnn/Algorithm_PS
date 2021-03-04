"""https://www.acmicpc.net/problem/2589"""


"""보물섬"""

from collections import deque


r , c = map(int,input().split())

board = [list(input()) for _ in range(r)]



def bfs(y,x,visited):

    q = deque([(y,x)])

    visited[y][x] = 1

    while q:

        node = q.popleft()

        for d in (-1,0),(1,0),(0,-1),(0,1):
            ny = node[0] + d[0]
            nx = node[1] + d[1]
            if 0<=ny<r and 0<=nx<c and visited[ny][nx] == 0 and board[ny][nx] == 'L':
                visited[ny][nx] = visited[node[0]][node[1]] + 1
                q.append((ny,nx))

    return max(map(max,visited))-1

result = -1

for i in range(r):
    for j in range(c):
        if board[i][j] == 'L':
            visited = [[0 for _ in range(c)] for _ in range(r)]
            result = max(bfs(i,j,visited),result)

print(result)





