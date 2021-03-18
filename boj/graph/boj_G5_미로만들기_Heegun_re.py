"""https://www.acmicpc.net/problem/2665"""


"""미로만들기"""


import sys
import heapq

INF = sys.maxsize


n = int(input())

board = [input() for _ in range(n)]
cost = [[INF]*n for _ in range(n)]

def d_solution(sy,sx,board,cost):
    q = []
    heapq.heappush(q,(0,(sy,sx)))
    cost[0][0] = 0

    while q:
        cnt, (y,x) = heapq.heappop(q)

        if y == n-1 and x == n-1:
            return cost[y][x]

        for d in [(-1,0),(0,1),(1,0),(0,-1)]:
            ny, nx = y+d[0], x+d[1]

            if 0<=ny<n and 0<=nx<n:

                if board[ny][nx] == '0':
                    if cost[ny][nx] > cnt + 1:
                        cost[ny][nx] = cnt + 1
                        heapq.heappush(q,(cnt+1,(ny,nx)))
                else:
                    if cost[ny][nx] > cnt:
                        cost[ny][nx] = cnt
                        heapq.heappush(q,(cnt,(ny,nx)))



    

print(d_solution(0,0,board,cost))


