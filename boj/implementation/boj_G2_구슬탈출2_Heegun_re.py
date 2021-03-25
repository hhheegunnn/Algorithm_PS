"""https://www.acmicpc.net/problem/13460"""


"""구슬탈출2"""

from collections import deque

N,M = map(int,input().split())

board = []

for _ in range(N):
    board.append(list(input()))

visited = set()


for i in range(N):
    for j in range(M):
        if board[i][j] == "R":
            red = [i,j]
        elif board[i][j] == "B":
            blue = [i,j]


def move(y,x,dy,dx):
    cnt = 0
    while board[y+dy][x+dx] != "#" and board[y][x] != "O":
        y,x = y+dy, x+dx
        cnt += 1
    return y,x,cnt


def solution(ry,rx,by,bx,ans):
    q = deque([(ry,rx,by,bx,ans)])
    visited.add((ry,rx,by,bx))

    while q:
        sry,srx,sby,sbx,ans = q.popleft()

        if ans > 10:
            return -1

        for dy,dx in [(0,1),(1,0),(-1,0),(0,-1)]:
            nry,nrx,rcnt = move(sry,srx,dy,dx)
            nby,nbx,bcnt = move(sby,sbx,dy,dx)


            if board[nby][nbx] != "O":
                if board[nry][nrx] == "O":
                    return ans
                if nby == nry and nbx == nrx:
                    if rcnt > bcnt:
                        nry,nrx = nry-dy,nrx-dx
                    else:
                        nby,nbx = nby-dy,nbx-dx
                if (nry,nrx,nby,nbx) not in visited:
                    visited.add((nry,nrx,nby,nbx))
                    q.append((nry,nrx,nby,nbx,ans+1))
    return -1

print(solution(red[0],red[1],blue[0],blue[1],1))

    
