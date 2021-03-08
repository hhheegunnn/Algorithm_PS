"""https://www.acmicpc.net/problem/2933"""


"""미네랄"""

from collections import deque


R,C = map(int,input().split())

board = [list(input()) for _ in range(R)]

N = int(input())

s_list = list(map(int,input().split()))


def check_drop(y,x):
    visited = set()
    q = deque([(y,x)])
    visited.add((y,x))
    drop_list = [[] for _ in range(C)]
    drop_list[x].append(y)

    while q:
        node_y,node_x = q.popleft()

        for dy, dx in [(1,0),(0,1),(-1,0),(0,-1)]:
            ny = node_y + dy
            nx = node_x + dx

            if 0<= ny < R and 0<= nx < C:
                if board[ny][nx] == 'x' and (ny,nx) not in visited:
                    visited.add((ny,nx))
                    q.append((ny,nx))
                    drop_list[nx].append(ny)


    for k,_ in visited:
        if k == R-1:
            return False
        else:  
            continue
    
    return drop_list


def drop(drop_list):
    #print(drop_list)
    drop_cnt_list = []

    for i in range(len(drop_list)):
        if drop_list[i]:
            max_r = max(drop_list[i])
            k = 1
            while True:
                if max_r + k >= R or board[max_r + k][i] == 'x':
                    break
                else:
                    k += 1
            drop_cnt_list.append(k-1)

    drop_cnt = min(drop_cnt_list)
    #print(drop_cnt_list)
    for i in range(len(drop_list)):
        for j in sorted(drop_list[i],reverse=True):
            board[j+drop_cnt][i] = 'x'
            board[j][i] = '.'





def solution():
    for r in range(R):
        for c in range(C):
            if board[r][c] == 'x' and (r,c) not in visited:
                #print(r,c)
                t = check_drop(r,c)
                if t == False:
                    continue
                else:
                    #print(r,c)
                    drop(t)
                    
                    return

def output():
    for r in range(R):
        print(''.join(board[r]))

for i in range(len(s_list)):

    h = R - s_list[i]

    if i%2 == 0:
        for j in range(C):
            if board[h][j] == 'x':
                board[h][j] = '.'
                break
    
    else:
        for j in range(C-1,-1,-1):
            if board[h][j] == 'x':
                board[h][j] = '.'
                break
    #print(board)
    visited = set()

    solution()

                    
output()

"""
4 4
...x
..xx
.xxx
xxxx
10
1 2 3 4 1 2 3 4 3 4
"""