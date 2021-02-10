"""https://www.acmicpc.net/problem/14502"""


""" 연구소 """

import copy
from itertools import combinations
from collections import deque


N, M = map(int,input().split())

board = [list(map(int,input().split())) for _ in range(N)]

def gas_position(board):
    g_position = []
    for i in range(N):
        for j in range(M):
            if board[i][j] == 2:
                g_position.append((i,j))
    return g_position

def zero_place(copyboard):
    cnt = 0
    for i in range(N):
        for j in range(M):
            if copyboard[i][j] == 0:
                cnt += 1

    return cnt

def wall_position(board):
    
    positions = []

    for i in range(N):
        for j in range(M):
            if board[i][j] == 0:
                positions.append((i,j))

    w_positions = list(combinations(positions,3))

    return w_positions

def spread_gas_bfs(copyboard,visited,start_r,start_c):
    

    q = deque([[start_r, start_c]])

    visited[start_r][start_c] = True

    while q:

        r,c = q.popleft()

        for dr,dc in (-1,0),(1,0),(0,1),(0,-1):

            nr = r + dr
            nc = c + dc

            if 0<= nr < N and 0<= nc < M and not visited[nr][nc]:
                
                if copyboard[nr][nc] == 0:

                    copyboard[nr][nc] = 2
                    visited[nr][nc] = True
                    q.append([nr,nc])

    

############################################

w_position = wall_position(board)
g_position = gas_position(board)

max_safe = -1

for wi in range(len(w_position)):

    copyboard = copy.deepcopy(board)

    for wii in range(3):
        r, c = w_position[wi][wii][0] , w_position[wi][wii][1]

        copyboard[r][c] = 1

    visited = [[False for _ in range(M)] for _ in range(N)]


    for i,j in g_position:
        spread_gas_bfs(copyboard,visited,i,j)


    cnt = zero_place(copyboard)

    max_safe = max(cnt,max_safe)

print(max_safe)