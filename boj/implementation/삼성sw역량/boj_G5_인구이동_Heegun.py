"""https://www.acmicpc.net/problem/16234"""


"""인구이동"""

from collections import deque

N, L, R = map(int,input().split())

board = [list(map(int,input().split())) for _ in range(N)]


def check_union(sr,sc,visited):

    union = []

    q = deque([(sr,sc)])

    visited[sr][sc] = True

    union.append((sr,sc))

    while q:

        r,c = q.popleft()


        for dr,dc in [(-1,0),(1,0),(0,1),(0,-1)]:

            nr = r + dr
            nc = c + dc


            if 0<= nr < N and 0<= nc < N:

                if L<= abs(board[r][c] - board[nr][nc]) <= R and not visited[nr][nc]:

                    visited[nr][nc] = True

                    union.append((nr,nc))

                    q.append((nr,nc))
    #print(union)
    return union

def move_pop(unions):

    population = 0

    for u in unions:
        for c in u:
            population += board[c[0]][c[1]]
        
        population = population//len(u)

        for c in u:
            board[c[0]][c[1]] = population

        population = 0
###### 안해주면 시간초과 
def diff_n(y,x):
    for i in [(-1,0),(1,0),(0,1),(0,-1)]:
        ny,nx = y+i[0], x+i[1]
        if 0<=ny<N and 0<= nx<N:
            if L <= abs(board[y][x] - board[ny][nx]) <= R:
                return True
      
    return False
####################
def solution():

    cnt = 0

    while True:

        unions = []

        visited = [[False for _ in range(N)] for _ in range(N)]

        flag = False

        for i in range(N):
            for j in range(N):
                if not visited[i][j] and diff_n(i,j): # diff_n을 통해 bfs실행을 줄임 
                    tmp = check_union(i,j,visited)

                    unions.append(tmp)

                    flag = True
        #print(unions)
        if flag:
            move_pop(unions)
            cnt += 1
            
        else:
            return cnt

            
        #print(board)

print(solution())




