"""https://www.acmicpc.net/problem/7576"""



"""토마토"""


# git add week_06/Re_boj_S1_7576_Heegun.py
# git commit -m "[김희건] boj 토마토 [bfs]"

from collections import deque
import sys

dir_y = [1,0,0,-1]
dir_x = [0,1,-1,0]

c, r = map(int,input().split())

board = list(list(map(int,input().split())) for _ in range(r))

visited = [[0]*c for _ in range(r)]

q = deque()

def check_in(y,x):
    if 0<= y < r and 0<= x <c:
        return True
    else:
        return False



def bfs():

    while q:

        y,x = q.popleft()
        for i in range(4):
            ny = y + dir_y[i]
            nx = x + dir_x[i]

            if check_in(ny,nx) and board[ny][nx] == 0 and visited[ny][nx] == 0:
                q.append([ny,nx])
                board[ny][nx] = 1
                visited[ny][nx] = visited[y][x] + 1





for i in range(r):
    for j in range(c):
        if board[i][j] == 1 and visited[i][j] == 0:
            q.append([i,j])
            visited[i][j] = 1


bfs()


for a in board:
    if 0 in a:
        print(-1)
        sys.exit()

cnt = 0

for i in visited:
    max_tmp = max(i)
    cnt = max(cnt,max_tmp)

print(cnt-1)

