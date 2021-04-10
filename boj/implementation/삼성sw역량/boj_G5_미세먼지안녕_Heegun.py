"""
https://www.acmicpc.net/problem/17144
미세먼지
""" 

from collections import deque


R,C,T = map(int,input().split())

board = [list(map(int,input().split())) for _ in range(R)]

air_cleaner = []

for i in range(R):
    if board[i][0] == -1:
        air_cleaner.append((i,0))
        air_cleaner.append((i+1,0))
        break


def spread_dust():

    tmp = [[0] * C for _ in range(R)]

    for r in range(R):
        for c in range(C):

            if board[r][c] >= 5:
                s_air = board[r][c]//5

                for d1,d2 in (1,0), (-1,0), (0,1), (0,-1):
                    sr = r+d1
                    sc = c+d2
                    if 0<= sr < R and 0<= sc < C and board[sr][sc] != -1:
                        tmp[sr][sc] += s_air
                        board[r][c] -= s_air

    for i in range(R):
        for j in range(C):
            board[i][j] += tmp[i][j]


def air_clean():
    ur, uc = air_cleaner[0][0], air_cleaner[0][1]
    dr, dc = air_cleaner[1][0], air_cleaner[1][1]


    tmp = deque()

    for c in range(C):
        tmp.append(board[ur][c])
    for r in range(ur-1,-1,-1):
        tmp.append(board[r][C-1])
    for c in range(C-2,-1,-1):
        tmp.append(board[0][c])
    for r in range(1,ur):
        tmp.append(board[r][0])

    tmp.rotate(1)

    for c in range(C):
        board[ur][c] = tmp.popleft()
    for r in range(ur-1,-1,-1):
        board[r][C-1]= tmp.popleft()
    for c in range(C-2,-1,-1):
        board[0][c] = tmp.popleft()
    for r in range(1,ur):
        board[r][0] = tmp.popleft()
    
    board[ur][uc] = -1
    board[ur][uc+1] = 0


    tmp_2 = deque()
    for c in range(C):
        tmp_2.append(board[dr][c])
    for r in range(dr+1,R):
        tmp_2.append(board[r][C-1])
    for c in range(C-2,-1,-1):
        tmp_2.append(board[R-1][c])
    for r in range(R-2,dr,-1):
        tmp_2.append(board[r][0])

    tmp_2.rotate(1)

    for c in range(C):
        board[dr][c] = tmp_2.popleft()
    for r in range(dr+1,R):
        board[r][C-1] = tmp_2.popleft()
    for c in range(C-2,-1,-1):
        board[R-1][c] = tmp_2.popleft()
    for r in range(R-2,dr,-1):
        board[r][0] = tmp_2.popleft()
    
    board[dr][dc] = -1
    board[dr][dc+1] = 0

def move_air(cr,dir):

    if dir == 1:
        # 1. 좌변
        for i in range(cr - 1, 0, -1):
            board[i][0]= board[i - 1][0]
        # 2. 윗변
        for j in range(0, C - 1):
            board[0][j] = board[0][j + 1]
        # 3. 우변
        for i in range(0, cr):
            board[i][C - 1] = board[i + 1][C - 1]
        # 4. 아래변
        for j in range(C - 1, 1, -1):
            board[cr][j] = board[cr][j - 1]
    else:
        for i in range(cr + 1, R - 1):
            board[i][0] = board[i + 1][0]
        for j in range(0, C - 1):
            board[R - 1][j] = board[R - 1][j + 1]
        for i in range(R - 1, cr, -1):
            board[i][C - 1] = board[i - 1][C - 1]
        for j in range(C - 1, 1, -1):
            board[cr][j] = board[cr][j - 1]
    board[cr][1] = 0


def solution():

    for _ in range(T):


        spread_dust()
        air_clean()
        #move_air(air_cleaner[0][0],1)
        #move_air(air_cleaner[1][0],0)

    return sum(map(sum, board))+2

print(solution())