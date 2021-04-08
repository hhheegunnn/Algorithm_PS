"""https://www.acmicpc.net/problem/15686"""


"""치킨배달"""


from itertools import combinations
from collections import deque
import sys


N , M = map(int,input().split())

board = [list(map(int,input().split())) for _ in range(N)]

ch_store = []
home = []

for i in range(N):
    for j in range(N):
        if board[i][j] == 2:
            ch_store.append((i,j))
        elif board[i][j] == 1:
            home.append((i,j))

remain_ch_store = list(combinations(ch_store,M))

"""
def bfs(sr,sc, store):
    #print(store)

    visited = [[-1 for _ in range(N)] for _ in range(N)]

    q = deque([(sr,sc)])
    visited[sr][sc] += 1

    while q:

        r,c = q.popleft()

        for dr,dc in [(1,0),(0,1),(-1,0),(0,-1)]:

            nr, nc = r+dr, c+dc

            if (0<= nr < N and 0<= nc < N) and visited[nr][nc] == -1:

                if (nr,nc) not in store:
                    q.append((nr,nc))
                    visited[nr][nc]  = visited[r][c] + 1

                else:
                    visited[nr][nc]  = visited[r][c] + 1
                    return visited[nr][nc]
"""


def solution():

    mn = sys.maxsize
    for store in remain_ch_store:

        cnt = 0

        for hr,hc in home:
            tmp = sys.maxsize
            for sr,sc in store:
                d = abs(hr-sr) + abs(hc-sc)
                tmp = min(tmp,d)
            cnt += tmp
        mn = min(mn,cnt)
        
    return mn


print(solution())

