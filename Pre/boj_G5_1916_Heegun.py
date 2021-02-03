"""https://www.acmicpc.net/problem/1916"""


"""최소비용 구하기"""

# git add week_11/boj_G5_1916_Heegun.py
# git commit -m "[김희건] boj 최소비용 구하기 [다익스트라 기본]"


import sys
import heapq

INF = sys.maxsize

input = sys.stdin.readline


def solution(start,end):
    q = []
    heapq.heappush(q,(0,start))
    distance[start] = 0

    while q:

        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = i[1] + dist

            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))

    return distance[end]



N = int(input())
M = int(input())
graph = [[] for _ in range(N+1)]
distance = [INF] * (N+1)

for _ in range(M):
    s,e,w = map(int,input().split())
    graph[s].append((e,w))

start_node,end_node = map(int,input().split())

print(solution(start_node,end_node))

