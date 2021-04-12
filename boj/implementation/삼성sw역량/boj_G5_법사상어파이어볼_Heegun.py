"""https://www.acmicpc.net/problem/20056"""


"""마법사 상어와 파이어볼"""

import math


N,M,K = map(int,input().split())

board = [[[]for _ in range(N)]for _ in range(N)]

for _ in range(M):

    r,c,m,s,d = map(int,input().split())

    board[r-1][c-1].append([m,s,d])

def step_2(t_board):

    for r in range(N):
        for c in range(N):
            ball_num = len(t_board[r][c])
            tmp = []
            if  ball_num >= 2:
                sum_m = 0
                sum_s = 0
                odd = False
                even = False
                for ball in t_board[r][c]:
                    sum_m += ball[0]
                    sum_s += ball[1]
                    if ball[2]%2==0:
                        even = True
                    else:
                        odd = True

                sp_m = math.floor(sum_m/5)
                sp_s = math.floor(sum_s/ball_num)

                if sp_m > 0:
                    if even and odd:
                        tmp.append([sp_m,sp_s,1])
                        tmp.append([sp_m,sp_s,3])
                        tmp.append([sp_m,sp_s,5])
                        tmp.append([sp_m,sp_s,7])
                    else:
                        tmp.append([sp_m,sp_s,0])
                        tmp.append([sp_m,sp_s,2])
                        tmp.append([sp_m,sp_s,4])
                        tmp.append([sp_m,sp_s,6])

                t_board[r][c] = tmp

            else:
                continue
    
    return t_board




def solution():
    global board

    dr =[-1,-1,0,1,1,1,0,-1]
    dc =[0,1,1,1,0,-1,-1,-1]

    for _ in range(K):

        tmp_board = [[[]for _ in range(N)]for _ in range(N)]

        for r in range(N):
            for c in range(N):

                if board[r][c]:

                    while board[r][c]:
                        tm,ts,td = board[r][c].pop()

                        nr,nc = r + dr[td]*ts, c + dc[td]*ts

                        if nr >= N:
                            nr = nr%N
                        if nc >= N:
                            nc = nc%N
                        if nr < 0:
                            nr = (N-(-nr)%N)%N
                        if nc < 0:
                            nc = (N-(-nc)%N)%N                     

                        tmp_board[nr][nc].append([tm,ts,td])


        board = step_2(tmp_board)

    
    result = 0

    for r in range(N):
        for c in range(N):
            if board[r][c]:
                for i in board[r][c]:
                    result += i[0] 



    return result
                    


print(solution())

"""
4 2 1
1 1 5 2 2
1 4 7 1 6
"""
