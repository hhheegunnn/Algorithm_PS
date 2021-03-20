"""https://www.acmicpc.net/problem/10282"""


"""해킹"""

import heapq
import sys

INF = sys.maxsize
input = sys.stdin.readline



def solution(start):

    q = []
    heapq.heappush(q,(0,start))
    cost[start] = 0


    while q:

        dist, node = heapq.heappop(q)

        if cost[node] < dist:
            continue

        for time,nn in graph[node]:

            if cost[nn] > dist + time:

                cost[nn] = dist + time

                heapq.heappush(q,(cost[nn],nn)) 
                
    cnt = 0
    sec = 0
    for cc in cost:
        if cc != INF:
            cnt += 1
            sec = max(sec,cc)
    print(cnt,sec)


for _ in range(int(input())):
    n,d,c = map(int,input().split())
    graph = [[] for _ in range(n+1)]
    cost = [INF for _ in range(n+1)]
    for _ in range(d):
        a,b,s = map(int,input().split())
        graph[b].append((s,a))
    
    solution(c)

    