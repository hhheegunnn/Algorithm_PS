"""https://www.acmicpc.net/problem/16236"""



"""아기상어"""

import heapq
from collections import deque

#####

N = int(input())

board = [list(map(int,input().split())) for _ in range(N)]

for i in range(N):
    for j in range(N):
        if board[i][j] == 9:
            shark_cord = [i,j]

shark = 2

#####

def bfs(sr,sc,shark):
    
    q = deque([(sr,sc)])

    visited = [[-1 for _ in range(N)] for _ in range(N)]

    visited[sr][sc] = 0

    eat_list = []

    while q:
        r,c = q.popleft()

        for dr,dc in [(-1,0),(0,1),(1,0),(0,-1)]:

            nr, nc = r+dr, c+dc

            if (0<= nr< N and 0 <= nc < N) and visited[nr][nc] == -1:
                if board[nr][nc] <= shark:
                    if board[nr][nc] == shark or board[nr][nc] == 0:
                        visited[nr][nc] = visited[r][c] + 1
                        q.append((nr,nc))
                    elif 0 < board[nr][nc] < shark:
                        visited[nr][nc] = visited[r][c] + 1
                        #eat_list.append((nr,nc,visited[nr][nc]))
                        heapq.heappush(eat_list,(visited[nr][nc],nr,nc))
                        continue

                else:
                    continue
    
    if eat_list:
        return heapq.heappop(eat_list)
    else:
        return []

            


def solution(shark_cord,shark):
    cnt = 0
    eat_cnt = 0
    while True:
        tmp = bfs(shark_cord[0],shark_cord[1],shark)
        
        if tmp:
            #print(tmp)
            board[shark_cord[0]][shark_cord[1]] = 0
            board[tmp[1]][tmp[2]] = 9
            shark_cord = [tmp[1],tmp[2]]
            eat_cnt += 1
            cnt += tmp[0]
        
        else:
            return cnt

        if shark == eat_cnt:
            shark += 1
            eat_cnt = 0

        #print(board)

print(solution(shark_cord,shark))


