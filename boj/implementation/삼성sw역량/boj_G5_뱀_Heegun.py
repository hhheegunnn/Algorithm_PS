"""https://www.acmicpc.net/problem/3190"""



"""뱀"""

##############################################

from collections import deque

N = int(input())

K = int(input())

board = [[0 for _ in range(N)] for _ in range(N)]

for _ in range(K):
    r,c = map(int,input().split())

    board[r-1][c-1] = 1

L = int(input())

chg_d = deque()

for _ in range(L):
    x,c = map(str, input().split())
    chg_d.append((int(x), c))

##############################################



def solution():
    
    d_list = [(-1,0), (0,1), (1,0), (0,-1)]

    snake = [ 1 , deque() ]
    snake[1].append((0,0))

    time = 0

    while True:

        time += 1
        head_d = snake[0]
        next_head_r = snake[1][-1][0] + d_list[head_d][0]
        next_head_c = snake[1][-1][1] + d_list[head_d][1]

        next_head = (next_head_r, next_head_c)

        if next_head in snake[1]:
            return time

        if 0<= next_head_r < N and 0<= next_head_c < N:

            snake[1].append(next_head)

            if board[next_head_r][next_head_c] == 1: 
                board[next_head_r][next_head_c] = 0
            else:
                snake[1].popleft()

        else:
            return time


        if chg_d:
            if time == chg_d[0][0]:
                if chg_d[0][1] == "L":
                    snake[0] = (snake[0]+3)%4
                else:
                    snake[0] = (snake[0]+1)%4

                chg_d.popleft()

    

print(solution())
