"""https://www.acmicpc.net/problem/20058"""


"""마법사 상어와 파이어스톰"""

from collections import deque


N , Q = map(int,input().split())


board = [list(map(int,input().split())) for _ in range(2**N)]

L_list = list(map(int,input().split()))


def spin(l,r,c,tmp):

    for i in range(2**l):
        for j in range(2**l):
            x, y = r+i, c+j
            tx = r + (j)
            ty = c + (2**l -1 - i)
            tmp[tx][ty] = board[x][y]

def check_near():
    #global board

    ice_list = []
    
    for r in range(2**N):
        for c in range(2**N):

            near_cnt = 0
            

            for dr, dc in [(0,1),(1,0),(0,-1),(-1,0)]:
                nr, nc = r + dr , c + dc

                if 0<= nr < 2**N and 0<= nc < 2**N:
                    if board[nr][nc] != 0:
                        near_cnt += 1
            
            if near_cnt < 3:
                if board[r][c] != 0:
                    ice_list.append((r,c))
                else:
                    continue

    for r,c in ice_list:
        board[r][c] -= 1

def bfs_iceburg(sr,sc,visited):

    q = deque([(sr,sc)])

    visited[sr][sc] = True

    cnt = 1

    while q:
        
        r,c = q.popleft()

        for dr,dc in [(-1,0),(0,1),(1,0),(0,-1)]:

            nr, nc = r + dr ,c + dc

            if 0<= nr < 2**N and 0<= nc < 2**N and not visited[nr][nc]:
                
                if board[nr][nc] != 0:

                    visited[nr][nc] = True
                    q.append((nr,nc))
                    cnt += 1

    return cnt

                



def solution():
    global board

    for l in L_list:
        tmp = [[0 for _ in range(2**N)] for _ in range(2**N)]
        for r in range(0,2**N,2**l):
            for c in range(0,2**N,2**l):
                spin(l,r,c,tmp)
        #print(tmp)
        board = tmp

        check_near()

    visited = [[False for _ in range(2**N)] for _ in range(2**N)]

    mx = -1e9
    #print(board)
    for r in range(2**N):
        for c in range(2**N):
            if not visited[r][c] and board[r][c] != 0:
                mx = max(mx,bfs_iceburg(r,c,visited))

    if mx == 1 or mx == -1e9:
        print(sum(map(sum,board)))
        print(0)
        return
    else:
        print(sum(map(sum,board)))
        print(mx)
        return

    
        
solution()

