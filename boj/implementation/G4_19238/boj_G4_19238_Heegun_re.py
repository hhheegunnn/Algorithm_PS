"""https://www.acmicpc.net/problem/19238"""


"""스타트 택시 """

from collections import deque
import heapq
import sys

def find_nearest_guest(sr,sc):

    visited = [[0 for _ in range(N)] for _ in range(N)]

    visited[sr][sc] = 1

    q = deque([(sr,sc,0)])

    guest_list = []

    min_d = -1

    if board[sr][sc] < 0:
        heapq.heappush(guest_list,(sr,sc,0,board[sr][sc]*-1-1))
        return heapq.heappop(guest_list)

    while q:

        y,x,dist = q.popleft()
        #print(y,x,dist,min_d)

        ## 택시 시작점에 손님이 있을때 



        if min_d != -1 and min_d <= dist:
            continue

        
        for dr,dc in (0,1),(1,0),(0,-1),(-1,0):
            ny = y+dr
            nx = x+dc
        
            if 0<= ny < N and 0<= nx < N:
                if board[ny][nx] != 1 and visited[ny][nx] == 0:
        
                    visited[ny][nx] = 1

                    if board[ny][nx] < 0:
                        heapq.heappush(guest_list,(ny,nx,dist+1,board[ny][nx]*-1-1))
                        min_d = dist + 1
                        #print(min_d)
                    else:
                        q.append((ny,nx,dist+1))

    
    if guest_list:
        return heapq.heappop(guest_list)
    else:
        return -1



def move(sr,sc,er,ec):

    visited = [[0 for _ in range(N)] for _ in range(N)]

    visited[sr][sc] = 1

    q = deque([(sr,sc,0)])

    while q:

        y,x,dist = q.popleft()
        
        for dr,dc in (0,1),(1,0),(0,-1),(-1,0):
            ny = y+dr
            nx = x+dc
        
            if 0<= ny < N and 0<= nx < N:
                if board[ny][nx] != 1 and visited[ny][nx] == 0:

                    if ny == er and nx == ec:
                        return dist+1

                    else:
                        visited[ny][nx] = 1
                        q.append((ny,nx,dist+1))
         
    return -1






N, M, total_oil = map(int,input().split())


board = [list(map(int,input().split())) for _ in range(N)]

sr,sc = map(int,input().split())

sr -= 1
sc -= 1

guest = []

for i in range(M):
    a,b,c,d = map(int,input().split())
    guest.append((a-1,b-1,c-1,d-1))
    board[a-1][b-1] = -(i+1)

flag = True
end_cnt = 0

while end_cnt < M:
    if find_nearest_guest(sr,sc) == -1:
        flag = False
        break
    else:
        y, x, use_oil, index = find_nearest_guest(sr,sc)

    if use_oil > total_oil:
        flag = False
        break
    else:
        total_oil -= use_oil
        sr, sc = y, x

    board[y][x] = 0

    er,ec = guest[index][2], guest[index][3]

    use_oil_move = move(sr,sc,er,ec)


    if use_oil_move == -1:
        flag = False
        break
    
    if use_oil_move > total_oil:
        flag = False
        break
    else:
        sr,sc = er,ec
        total_oil -= use_oil_move
        total_oil += (use_oil_move*2)
        end_cnt += 1

if flag:
    print(total_oil)
else:
    print(-1)











"""
6 3 15
0 0 1 0 0 0
0 0 1 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 1 0
0 0 0 1 0 0
6 5
6 5 5 6
5 4 1 6
4 2 3 5
"""