"""https://www.acmicpc.net/problem/19236"""


""" 청소년 상어 """

import copy

direc = [(-1,0), (-1,-1), (0,-1), (1,-1), (1,0), (1,1), (0,1), (-1,1)]

result = 0

board = []

for _ in range(4):
    tmp = list(map(int,input().split()))

    k = []
    for i in range(4):
        k.append([tmp[2*i], tmp[2*i+1]-1])
    
    board.append(k)


def find_fish(board,index):
    for i in range(4):
        for j in range(4):
            if board[i][j][0] == index:
                return (i,j)

    return False


def move_fish(board,shark_r,shark_c):

    position = []

    for i in range(1,17):
        position = find_fish(board,i)

        if not position:
            continue

        r,c = position[0],position[1]

        d = board[r][c][1]

        for _ in range(8):
            next_r = r + direc[d][0]
            next_c = c + direc[d][1]

            if 0<= next_r < 4 and 0<= next_c < 4:
                if not (next_r == shark_r and next_c == shark_c):
                    board[r][c][0], board[next_r][next_c][0] = board[next_r][next_c][0], board[r][c][0]
                    board[r][c][1], board[next_r][next_c][1] = board[next_r][next_c][1], d
                    break

            d = (d+1) % 8

def food(board,shark_r,shark_c):
    positions = []
    d = board[shark_r][shark_c][1]

    for _ in range(1,4):
        next_r = shark_r + direc[d][0]  
        next_c = shark_c + direc[d][1]

        if 0 <= next_r < 4 and 0<= next_c < 4 and 1 <= board[next_r][next_c][0] <= 16:
            positions.append([next_r,next_c])

        shark_r, shark_c = next_r, next_c
    
    return positions



def dfs(board,shark_r,shark_c,total):
    global result

    a = copy.deepcopy(board)

    number = a[shark_r][shark_c][0]
    a[shark_r][shark_c][0] = -1

    move_fish(a,shark_r,shark_c)

    food_list = food(a,shark_r,shark_c)

    result = max(result, total+number)

    for nr , nc in food_list:
        dfs(a,nr,nc,total+number)




###################################




dfs(board,0,0,0)
print(result)


######################################

