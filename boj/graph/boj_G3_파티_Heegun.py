"""https://www.acmicpc.net/problem/1238"""


"""퍄티"""

import heapq
import sys

INF = sys.maxsize

N, M, X = map(int,input().split())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    s,e,c = map(int,input().split())
    graph[s].append((c,e))


def solution(start,end,graph):
    cost = [INF for _ in range(N+1)]
    q = []
    heapq.heappush(q,(0,start))
    cost[start] = 0

    while q:
        st, node = heapq.heappop(q)

        if node == end:
            #print(cost[end])
            return cost[end]

        if cost[node] < st:
            continue

        for time,next_node in graph[node]:

            if cost[next_node] > st+time:
                cost[next_node] = st+time

                heapq.heappush(q,(cost[next_node],next_node))


max_time = -1
for i in range(1,N+1):
    if i != X: 
        go = solution(i,X,graph)
        back = solution(X,i,graph)
        max_time = max(max_time,go+back)
    else:
        continue

print(max_time)


