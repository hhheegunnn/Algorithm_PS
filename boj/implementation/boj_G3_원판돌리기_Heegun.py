"""https://www.acmicpc.net/problem/17822"""


"""원판 돌리기"""

from collections import deque

# N 원판 개수
N,M,T = map(int,input().split())

board = [[]]


def spin(board,command_list):
    x, d, k = command_list[0], command_list[1], command_list[2]
    for i in range(x,N+1,x):
        tmp = deque(board[i][1:M+1])
        if d == 0:
            tmp.rotate(k)
        else:
            tmp.rotate(-k)
        board[i] = [0] + list(tmp)


def erase_and_processing(board):

    erase_cord = set()


    for i in range(1,N+1):
        for j in range(1,M+1):
            #tmp = board[i][j]
            if board[i][j] != 0:
                if j == 1:
                    if board[i][2] == board[i][1]:
                        erase_cord.add((i,j))
                        erase_cord.add((i,2))
                    if board[i][M] == board[i][1]:
                        erase_cord.add((i,j))
                        erase_cord.add((i,M))
                elif j == M:
                    if board[i][M-1] == board[i][M]:
                        erase_cord.add((i,j))
                        erase_cord.add((i,M-1))
                    if board[i][1] == board[i][M]:
                        erase_cord.add((i,j))
                        erase_cord.add((i,1))
                else:
                    if board[i][j-1] == board[i][j]:
                        erase_cord.add((i,j))
                        erase_cord.add((i,j-1))
                    if board[i][j+1] == board[i][j]:
                        erase_cord.add((i,j))
                        erase_cord.add((i,j+1))
                
                if i == 1:
                    if board[2][j] == board[1][j]:
                        erase_cord.add((i,j))
                        erase_cord.add((2,j))
                elif i == N:
                    if board[N-1][j] == board[N][j]:
                        erase_cord.add((i,j))
                        erase_cord.add((N-1,j))
                else:
                    if board[i-1][j] == board[i][j]:
                        erase_cord.add((i,j))
                        erase_cord.add((i-1,j))
                    if board[i+1][j] == board[i][j]:
                        erase_cord.add((i,j))
                        erase_cord.add((i+1,j))

    if erase_cord:
        for y,x in erase_cord:

            board[y][x] = 0
    else:
        cnt = 0

        for i in range(1,N+1):
            cnt = cnt + (M - board[i][1:].count(0))
        
        if cnt == 0:
            avg_ = 0

        else:
            avg_ = sum(map(sum,board[1:]))/cnt

        for i in range(1,N+1):
            for j in range(1,M+1):
                if board[i][j] != 0:
                    if board[i][j] > avg_:
                        board[i][j] -= 1
                    elif board[i][j] < avg_:
                        board[i][j] += 1



for _ in range(N):
    t = list(map(int,input().split()))
    board.append([0]+t)


for _ in range(T):
    command_list= list(map(int,input().split()))
    spin(board,command_list)
    erase_and_processing(board)

#print(board)
result = sum(map(sum,board[1:]))
print(result)




