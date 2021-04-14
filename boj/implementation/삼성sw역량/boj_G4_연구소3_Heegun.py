"""https://www.acmicpc.net/problem/17142"""


"""연구소 3 """

from itertools import combinations
from collections import deque
import copy

N, M = map(int,input().split())

board = [list(map(int,input().split())) for _ in range(N)]

all_viruses = []
empty = 0

for r in range(N):
    for c in range(N):
        if board[r][c] == 2:
            all_viruses.append((r,c))
        elif board[r][c] == 0:
            empty += 1


M_virus = list(combinations(all_viruses,M))


def spread_bfs(viruses,no_active_virus,copyboard,empty):

    for r,c in viruses:
        copyboard[r][c] = 0

    q = deque(viruses)

    time = 0

    while q:

        if empty == 0:
            break

        r,c = q.popleft()

        for dr,dc in [(-1,0),(0,1),(1,0),(0,-1)]:

            nr , nc = r + dr, c + dc

            if 0<= nr < N and 0<= nc < N:

                if copyboard[nr][nc] == 0 and (nr,nc) not in viruses:
                    copyboard[nr][nc] = copyboard[r][c] + 1
                    time = copyboard[r][c] + 1
                    q.append((nr,nc))
                    empty -= 1

                if copyboard[nr][nc] == 2 and (nr,nc) in no_active_virus:
                    if empty:
                        copyboard[nr][nc] = copyboard[r][c] + 1
                        time = copyboard[r][c] + 1
                        q.append((nr,nc))
                    else:
                        copyboard[nr][nc] = copyboard[r][c]

    if empty == 0:          
        return time
    else:
        return 1e9


def solution():
    #print(M_virus)

    mn = 1e9
    result = 0


    
    for viruses in M_virus:

        copyboard = copy.deepcopy(board)
        no_active_virus = list(set(all_viruses) - set(viruses))
        result = spread_bfs(viruses,no_active_virus,copyboard,empty)

        if result != 1e9:
            mn = min(mn,result)
    
    if mn == 1e9:
        return -1
    else:
        return mn

        

print(solution())

"""
3 1
0 2 1
0 1 0
0 0 2
"""

    