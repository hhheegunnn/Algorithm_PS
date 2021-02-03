"""https://www.acmicpc.net/problem/2573"""


"""  빙산 """

# git add boj_implementation/G/G4/2573/Re_boj_G4_2573_Heegun.py
# git commit -m "[김희건] boj 빙산 [pypy3 통과]"

from collections import deque
import sys


def bfs(sr,sc):

    q = deque([[sr,sc]])

    bfs_visited[sr][sc] = True
    

    while q:
        cnt = 0
        r,c = q.popleft()

        for dr, dc in (-1, 0), (0, 1), (1, 0), (0, -1):
            nr = r + dr
            nc = c + dc

            if 0<= nr < N and 0<= nc < M and not bfs_visited[nr][nc]:
                
                if board[nr][nc] != 0:
                    bfs_visited[nr][nc] = True
                    #board[nr][nc] += 1
                    q.append([nr,nc])

                elif board[nr][nc] == 0:
                    cnt += 1
        #print(board[r][c],cnt)
        if board[r][c] - cnt < 0:
            board[r][c]=0
        else:
            board[r][c] -= cnt

def check_zero():
    tmp = 0
    for i in board:
        tmp += sum(i)
        

    if tmp == 0:
        return True
    else:
        return False



N, M = map(int, input().split())
# N = R  # M = C

board = [list(map(int, input().split())) for _ in range(N)]



year_cnt = 0


while True:

    ice_cnt = 0
    bfs_visited = [[False for _ in range(M)] for _ in range(N)]

    for i in range(N):
        for j in range(M):
            if board[i][j] != 0:
                if not bfs_visited[i][j]:
                    bfs(i,j)
                    ice_cnt += 1
                    if ice_cnt >= 2:
                        print(year_cnt)
                        sys.exit(0)
                    elif ice_cnt == 1 and check_zero():
                        print(0)
                        sys.exit(0)
                    
    year_cnt += 1




