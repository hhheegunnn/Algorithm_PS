"""https://www.acmicpc.net/problem/16236"""


""" 아기 상어 """


# git add boj_implementation/G/G4/16236/boj_G4_16236_Heegun.py
# git commit -m "[김희건] boj 아기 상어 [bfs, heapq]"

from collections import deque
import heapq

delta = [(-1,0),(0,1),(1,0),(0,-1)]



def bfs(sy,sx,shark,shark_cnt,total_time):

    time = [[-1 for _ in range(N)] for _ in range(N)]

    q = deque()
    fish = []

    q.append([sy,sx])

    time[sy][sx] += 1 

    while q:
        
        py,px = q.popleft()


        for dy,dx in delta:
            ny = py + dy
            nx = px + dx

            if 0<= ny < N and 0<= nx < N and time[ny][nx] == -1:

                if 0 < board[ny][nx] < shark:
                    q.append([ny,nx])
                    time[ny][nx] = time[py][px] + 1
                    heapq.heappush(fish,(time[ny][nx], ny, nx))

                elif board[ny][nx] == 0 or board[ny][nx] == shark:
                    q.append([ny,nx])
                    time[ny][nx] = time[py][px] + 1
                else:
                    continue
    

    if fish:
        t,y,x = heapq.heappop(fish)
        shark_cnt += 1
        board[y][x] = 0
        total_time += t
        if shark == shark_cnt:
            shark += 1
            shark_cnt = 0
        return y,x,shark,shark_cnt,total_time

    
   
    return 0,0,0,0,total_time

                    

N = int(input())

shark = 2
shark_cnt = 0
total_time = 0

board = [list(map(int,input().split())) for _ in range(N)]

for y in range(N):
    for x in range(N):
        if board[y][x] == 9 :
            sy = y
            sx = x
            board[sy][sx] = 0
            


while True:
    sy,sx,shark,shark_cnt,total_time = bfs(sy,sx,shark,shark_cnt,total_time)
    if sy == 0 and sx == 0 and shark == 0 and shark_cnt == 0:
        print(total_time)
        break

