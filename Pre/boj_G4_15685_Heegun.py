"""https://www.acmicpc.net/problem/15685"""


""" 드래곤 커브 """

# git add boj_implementation/G/G4/15685/boj_G4_15685_Heegun.py
# git commit -m "[김희건] boj 드래곤 커브"

from collections import deque

delta =[(0,1),(-1,0),(0,-1),(1,0)]

find_s = [(0,1),(1,0),(0,-1)]

def draw(x,y,d,g):

    d_list = [d]

    for _ in range(g):
        lend = len(d_list)
        for j in range(lend-1,-1,-1):
            tmp = (d_list[j] + 1)%4
            d_list.append(tmp)

    for dt in d_list:

        board[y][x] = 1

        y = y + delta[dt][0]
        x = x + delta[dt][1]

        if 0<= y < k and 0<= x<k:

            if board[y][x] == 0:
                board[y][x] = 1
        

def find_square():

    s_cnt = 0
    

    for r in range(k):
        for c in range(k):
            cnt = 0
            if board[r][c] == 1:
                #print(r,c)
                tr = r
                tc = c
                for dr,dc in find_s:

                    nr = tr + dr
                    nc = tc + dc

                    if 0<= nr < k and 0<= nc < k and board[nr][nc]==1:
                        cnt += 1
                        tr = nr
                        tc = nc
                    else:
                        break
                if cnt == 3:
                    s_cnt += 1


                    
    return s_cnt




N = int(input())

k = 101

board = [[0 for _ in range(k)] for _ in range(k)]


for _ in range(N):
    x,y,d,g = map(int,input().split())
    draw(x,y,d,g)

#print(board)

print(find_square())

"""
6
1 1 0 0
1 2 0 0
1 3 0 0
2 1 0 0
2 2 0 0
2 3 0 0

"""










"""
3
3 3 0 1
4 2 1 3
4 2 2 1
"""