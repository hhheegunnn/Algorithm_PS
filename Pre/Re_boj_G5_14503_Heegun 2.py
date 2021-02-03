"""https://www.acmicpc.net/problem/14503"""


"""로봇청소기"""


# 북동남서
dx = [-1,0,1,0]
dy = [0,1,0,-1]
N, M = map(int,input().split())

r,c,d = map(int,input().split())


board = [list(map(int,input().split())) for _ in range(N)]


"""
ans = 0
def clean(r,c,d):
    global ans
    if board[r][c] == 0:
        board[r][c] = 2
        ans += 1
    for _ in range(4):
        nd = (d+3)%4
        nr = r + dx[nd]
        nc = c + dy[nd]
        if board[nr][nc] == 0:
            clean(nr,nc,nd)
            return
        d = nd
    
    nd = (d+2) %4
    nr = r + dx[nd]
    nc = c + dy[nd]
    if board[nr][nc] == 1:
        return
    clean(nr,nc,d)

clean(r,c,d)
print(ans)
"""


def turn_left(d):
    if(d == 0):
        return 3
    elif(d == 1):
        return 0
    elif(d == 2):
        return 1
    elif(d == 3):
        return 2

def clean(r,c,d):
    cnt = 1
    board[r][c] = 2
    while True:
        nd = d
        for _ in range(4):
            empty = 0
            nd = turn_left(nd)
            nr = r + dx[nd]
            nc = c + dy[nd]

            if board[nr][nc] == 0:
                cnt += 1
                r = nr
                c = nc
                board[nr][nc] = 2
                d = nd
                empty = 1
                break
        
        if empty == 0:
            if d == 0:
                r += 1
            elif d == 1:
                c -= 1
            elif d == 2:
                r -= 1
            elif d == 3:
                c += 1

            if board[r][c] == 1:
                break
    
    return cnt

ans = clean(r,c,d)
print(ans)



