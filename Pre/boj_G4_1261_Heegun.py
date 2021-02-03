"""https://www.acmicpc.net/problem/1261"""


"""알고스팟"""

# git add week_11/boj_G4_1261_Heegun.py
# git commit -m "[김희건] boj 알고스팟"

import heapq
INF = int(1e9)

direction = [(1,0),(0,1),(-1,0),(0,-1)]

def check_in(y,x):
    if 0<= x < M and 0<= y < N:
        return True
    else:
        return False


def solution(r,c,board,cost):
    
    q = []
    heapq.heappush(q,(0,(0,0)))
    cost[0][0] = 0

    while q:
        cnt , (j,i) = heapq.heappop(q)

        if j == r-1 and i == c-1:
            return cost[j][i]
        
        for d in range(4):
            y, x = j + direction[d][1], i + direction[d][0]

            if check_in(y,x):
                
                if board[y][x] == '1':
                    if cost[y][x] > cnt + 1:
                        cost[y][x] = cnt + 1
                        heapq.heappush(q,(cnt+1,(y,x)))
                else:
                    if cost[y][x] > cnt:
                        cost[y][x] = cnt
                        heapq.heappush(q,(cnt,(y,x)))



M,N = map(int,input().split())
# M c x열 개수  # N r y행 개수 
Board = [input() for _ in range(N)]

Cost = [[INF]*M for _ in range(N)]

print(solution(N,M,Board,Cost))

