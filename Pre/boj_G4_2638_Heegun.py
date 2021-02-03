"""https://www.acmicpc.net/problem/2638"""

""" 치즈 """

# git add boj_implementation/G/G4/2638/boj_G4_2638_Heegun.py
# git commit -m "[김희건] boj 치즈"


from collections import deque
left = 0


def bfs_out(sr, sc):

    q = deque([(sr, sc)])
    visited[sr][sc] = True
    board[sr][sc] = 3
    tmp = []

    while q:

        r, c = q.popleft()

        for dr, dc in (-1, 0), (1, 0), (0, -1), (0, 1):
            nr = r + dr
            nc = c + dc

            if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc]:

                visited[nr][nc] = True

                if board[nr][nc] == 1:
                    board[nr][nc] = 2
                    tmp.append((nr, nc))

                else:
                    board[nr][nc] = 3
                    q.append((nr, nc))

    return tmp


def check(sr, sc):

    cnt = 0

    for dr, dc in (-1, 0), (1, 0), (0, -1), (0, 1):
        nr = sr + dr
        nc = sc + dc

        if 0 <= nr < N and 0 <= nc < M:
            if board[nr][nc] == 3:
                cnt += 1

    if cnt >= 2:
        board[sr][sc] = 2
    else:
        board[sr][sc] = 1


def delete():
    global left
    for i in range(N):
        for j in range(M):
            if board[i][j] == 2:
                board[i][j] = 3
                left -= 1


N, M = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(N)]


for i in range(N):
    for j in range(M):
        if board[i][j] == 1:
            left += 1

kcnt = 0


while left != 0:

    kcnt += 1

    visited = [[False for _ in range(M)] for _ in range(N)]

    t = bfs_out(0, 0)

    for r, c in t:
        check(r, c)

    delete()


print(kcnt)

"""
5 5
0 0 0 0 0
0 1 1 1 0
0 1 0 1 0
0 1 1 1 0
0 0 0 0 0

"""
