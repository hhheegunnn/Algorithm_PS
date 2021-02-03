"""https://www.acmicpc.net/problem/11660"""


"""구간 합 구하기 5"""


# git add week_08/Re_boj_S1_11660_Heegun.py
# git commit -m "[김희건] boj 구간 합 구하기 5 [누적합 라이브러리, sys.stdin 미사용시 시간초과"

from itertools import accumulate
import sys

input = sys.stdin.readline

n,m = map(int,input().split())

board = []


for _ in range(n):
    board.append(list(map(int,input().split())))


for i in range(n):
    board[i] = list(accumulate(board[i]))
for y in range(1,n):
    for x in range(n):
        board[y][x] += board[y-1][x]


result = []

for _ in range(m):

    x1, y1, x2, y2 = map(int,input().split())

    if x1 == 1 and y1 == 1:
        print(board[x2-1][y2-1])
    elif x1 == 1:
        tmp = board[x2-1][y2-1] - board[x2-1][y1-2]
        print(tmp)
    elif y1 == 1:
        tmp = board[x2-1][y2-1] - board[x1-2][y2-1]
        print(tmp)
    else:
        tmp = board[x2-1][y2-1] - board[x2-1][y1-2] - board[x1-2][y2-1]
        tmp += board[x1-2][y1-2]
        print(tmp)











    



            









