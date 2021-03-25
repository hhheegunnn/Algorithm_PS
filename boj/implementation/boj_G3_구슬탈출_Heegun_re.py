"""https://www.acmicpc.net/problem/13459"""


"""구슬탈출"""

from collections import deque


N,M = map(int,input().split())


board = [list(input()) for _ in range(N)]

visited = set()

for i in range(N):
    for j in range(M):
        if board[i][j] == "R":
            ry,rx = i,j
        elif board[i][j] == "B":
            by,bx = i,j

def move(y,x,dy,dx):
    cnt = 0

    while True:
        
        if board[y+dy][x+dx] == "#" :
            break

        else:
            y = y+dy
            x = x+dx
            cnt += 1

        if board[y][x] == "O":
            break

    
    return y,x,cnt



def bfs(sry,srx,sby,sbx,ans):

    q = deque([])
    q.append((sry,srx,sby,sbx,ans))

    visited.add((sry,srx,sby,sbx))


    while q:


        ry,rx,by,bx,ans = q.popleft()

        if ans > 10:
            return 0

        for dy,dx in [(0,-1),(1,0),(0,1),(-1,0)]:
            nry, nrx, rcnt = move(ry,rx,dy,dx)
            nby, nbx, bcnt = move(by,bx,dy,dx)

            #print(nry,nrx)

            if board[nby][nbx] != "O":
                if board[nry][nrx] == "O":
                    return 1

                if nry==nby and nrx==nbx:
                    if rcnt > bcnt:
                        nry -= dy
                        nrx -= dx
                    else:
                        nby -= dy
                        nbx -= dx

                if (nry,nrx,nby,nbx) not in visited:
                    visited.add((nry,nrx,nby,nbx))
                    q.append((nry,nrx,nby,nbx,ans+1))

    return 0

print(bfs(ry,rx,by,bx,1))
                




