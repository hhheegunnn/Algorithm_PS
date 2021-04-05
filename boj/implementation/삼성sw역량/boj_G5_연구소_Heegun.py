"""https://www.acmicpc.net/problem/14502"""


"""연구소"""




from itertools import combinations
from copy import deepcopy
from collections import deque


####################

N,M = map(int,input().split())


board_og = [list(map(int,input().split())) for _ in range(N)]

#####################

wall_possible = []
virus = []

for i in range(N):
    for j in range(M):
        if board_og[i][j] == 0:
            wall_possible.append((i,j))
        elif board_og[i][j] == 2:
            virus.append((i,j))

wall_list = list(combinations(wall_possible,3))


def bfs(board,vr,vc,visited):

    q = deque([(vr,vc)])
    visited[vr][vc] = True


    while q:

        r,c = q.popleft()

        for dr,dc in [(0,1),(0,-1),(1,0),(-1,0)]:

            nr,nc = r+dr, c+dc

            if 0<= nr < N and 0<= nc < M:
                if board[nr][nc] == 0 and visited[nr][nc] == False:

                    board[nr][nc] = 2

                    visited[nr][nc] = True

                    q.append((nr,nc))    


def count_safe(board):

    cnt = 0

    for i in range(N):
        for j in range(M):

            if board[i][j] == 0:
                cnt += 1

    return cnt


def solution(wall_list,board_og):

    mx = 0
    
    for wall in wall_list:
        board = deepcopy(board_og)
        for wr,wc in wall:
            board[wr][wc] = 1

        visited = [[False for _ in range(M)] for _ in range(N)]

        for vr,vc in virus:
            bfs(board,vr,vc,visited)

        mx = max(mx,count_safe(board))

    return mx

print(solution(wall_list,board_og))
