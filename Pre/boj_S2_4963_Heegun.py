"""https://www.acmicpc.net/problem/4963"""


"""섬의 개수"""

#git add week_04/boj_S2_4963_Heegun.py

#git commit -m "[김희건] boj 섬의 개수 [파이썬 재귀 깊이 한계]"


import sys

sys.setrecursionlimit(2501)

def check_in(r,c):
    if 0<=r<h and 0<=c<w:
        return True
    else:
        return False

def dfs(r,c):

    board[r][c] = 0

    if check_in(r+1,c) and board[r+1][c] == 1:
        dfs(r+1,c)
    if check_in(r-1,c) and board[r-1][c] == 1:
        dfs(r-1,c)
    if check_in(r,c+1) and board[r][c+1] == 1:
        dfs(r,c+1)
    if check_in(r,c-1) and board[r][c-1] == 1:
        dfs(r,c-1)
    if check_in(r+1,c+1) and board[r+1][c+1] == 1:
        dfs(r+1,c+1)
    if check_in(r+1,c-1) and board[r+1][c-1] == 1:
        dfs(r+1,c-1)
    if check_in(r-1,c+1) and board[r-1][c+1] == 1:
        dfs(r-1,c+1)
    if check_in(r-1,c-1) and board[r-1][c-1] == 1:
        dfs(r-1,c-1)


result = []

while True:
    cnt = 0

    w,h = map(int,input().split())

    if w == 0 and h == 0:
        break

    board = [list(map(int,input().split())) for _ in range(h)]

    for i in range(h):
        for j in range(w):
            if board[i][j] == 1:
                dfs(i,j)
                cnt += 1
            else:
                continue

    result.append(cnt)

for i in result:
    print(i)