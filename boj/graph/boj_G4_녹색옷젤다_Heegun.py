"""https://www.acmicpc.net/problem/4485"""


"""녹색 옷 입은 애가 젤다지?"""

import sys
import heapq

INF = sys.maxsize

def solution(board,cost,sy,sx):
    cost[sy][sx] = board[sy][sx]


    q = []

    heapq.heappush(q,(cost[sy][sx],(sy,sx)))


    while q:

        dist, (y,x) = heapq.heappop(q)

        if y == N-1 and x == N-1:
            return cost[y][x]

        for dy,dx in [(1,0),(0,1),(-1,0),(0,-1)]:

            ny, nx = y+dy, x+dx

            if 0<=ny<N and 0<=nx<N:

                if cost[ny][nx] > dist+board[ny][nx]:

                    cost[ny][nx] = dist+board[ny][nx]

                    heapq.heappush(q,(cost[ny][nx],(ny,nx)))


case_num = 1
while True:

    N = int(input())

    if N == 0:
        break

    else:
        
        board = [list(map(int,input().split())) for _ in range(N)]
        cost = [[INF for _ in range(N)] for _ in range(N)]

        result = solution(board,cost,0,0)
        print('Problem {0}: {1}'.format(case_num,result))

    case_num += 1

