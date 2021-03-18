"""https://www.acmicpc.net/problem/1753"""


"""최단경로"""

import sys
import heapq

INF = sys.maxsize

V , E = map(int,input().split())

K = int(input())

graph = [[] for _ in range(V+1)]

distance = [INF for _ in range(V+1)] 

for _ in range(E):
    u,v,w = map(int,input().split())

    graph[u].append((w,v))


def dijkstra(start):

    q = []

    heapq.heappush(q,(0,start))
    distance[start] = 0

    while q:

        dist , now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[0]

            if cost < distance[i[1]]:
                distance[i[1]] = cost
                heapq.heappush(q,(cost,i[1]))


dijkstra(K)

for i in range(1,V+1):

    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])