"""https://www.acmicpc.net/problem/17779"""



"""게리맨더링 2"""


import sys


def sum_1(r,c,d1,d2,board):

    pop_1 = 0
    for i in range(r+d1):
        for j in range(c+1):
            pop_1 += board[i][j]

    t = -1
    for i in range(r,r+d1):
        t += 1
        for j in range(c-t,c+1):
            pop_1 -= board[i][j]

    return pop_1

def sum_2(r,c,d1,d2,board):

    pop_2 = 0
    for i in range(r+d2+1):
        for j in range(c+1,N):
            pop_2 += board[i][j]

    t = 0
    for i in range(r+1,r+d2+1):
        t += 1
        for j in range(c+1,c+1+t):
            pop_2 -= board[i][j]

    return pop_2

def sum_3(r,c,d1,d2,board):

    pop_3 = 0
    for i in range(r+d1,N):
        for j in range(c-d1+d2):
            pop_3 += board[i][j]

    t = -1
    for i in range(r+d1,r+d1+d2+1):
        t += 1
        for j in range(c-d1+t,c-d1+d2):
            pop_3 -= board[i][j]

    return pop_3

def sum_4(r,c,d1,d2,board):

    pop_4 = 0
    for i in range(r+d2+1,N):
        for j in range(c+d2-d1,N):
            pop_4 += board[i][j]

    t = -1

    for i in range(r+d2+1, r+d2+d1+1):
        t += 1
        for j in range(c+d2-d1,c+d2-t):
            pop_4 -= board[i][j]

    return pop_4



N = int(input())

board = [list(map(int,input().split())) for _ in range(N)]

total_sum = 0

for i in board:
    total_sum += sum(i)

minvalue = sys.maxsize

for r in range(N):
    for c in range(N):
        for d1 in range(1,N):
            for d2 in range(1,N):
                if (0 <= r+d1 < N and 0 <= c-d1 < N) and (0 <= r+d2 < N and 0 <= c+d2 < N) and (0 <= r+d1+d2 < N and 0 <= c-d1+d2 < N):
                    a = []
                    a.append(sum_1(r,c,d1,d2,board))
                    a.append(sum_2(r,c,d1,d2,board))
                    a.append(sum_3(r,c,d1,d2,board))
                    a.append(sum_4(r,c,d1,d2,board))
                    a.append(total_sum - sum(a))
                    a.sort() #값이 5개밖에 안되므로 정렬해주자
                    if minvalue > a[-1]-a[0]:
                        minvalue = a[-1]-a[0]


print(minvalue)


"""
6
1 2 3 4 1 6
7 8 9 1 4 2
2 3 4 1 1 3
6 6 6 6 9 4
9 1 9 1 9 5
1 1 1 1 9 9
"""