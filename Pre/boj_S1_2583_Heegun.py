"""https://www.acmicpc.net/problem/2583"""



"""영역 구하기"""


# git add week_06/boj_S1_2583_Heegun.py
# git commit -m "[김희건] boj 영역 구하기"

import sys

sys.setrecursionlimit(100000000)


r,c,k = map(int,input().split())

board = [[0]*c for _ in range(r)]



for _ in range(k):
    c1,r1,c2,r2 = map(int,input().split())

    cc = c2-c1
    rr = r2-r1

    for i in range(r1,r1+rr):
        for j in range(c1,c1+cc):
            board[i][j] = 1

#print(board)

cnt = 0

def check_in(y,x):
    if 0<= x < c and 0<= y < r:
        return True
    else:
        return False

def dfs(y,x):
    global cnt
    board[y][x] = 1
    cnt += 1
    if check_in(y+1,x) and board[y+1][x] == 0:
        dfs(y+1,x)
    if check_in(y,x+1) and board[y][x+1] == 0:
        dfs(y,x+1)
    if check_in(y-1,x) and board[y-1][x] == 0:
        dfs(y-1,x)
    if check_in(y,x-1) and board[y][x-1] == 0:
        dfs(y,x-1)
    
    return cnt
    
    
    

cntt = 0
result = []

for i in range(r):
    for j in range(c):
        if board[i][j] == 0:
            cnt = 0
            result.append(dfs(i,j))
            cntt += 1

print(cntt)
result.sort()
print(* result)


