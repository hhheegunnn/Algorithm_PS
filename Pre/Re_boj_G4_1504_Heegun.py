"""https://www.acmicpc.net/problem/1504"""


"""특정한 최단 경로"""


# git add week_11/Re_boj_G4_1504_Heegun.py
# git commit -m "[김희건] boj 특정한 최단 경로 [양방향, -1 출력 조건, 파이썬 and]"

import sys
import heapq
input = sys.stdin.readline
INF = sys.maxsize

def solution(start):
    # 1 시작 v1 -> v2 -> N
    # 2 시작 v2 -> v1 -> N
    distance = [INF] * (N+1)

    q = []
    heapq.heappush(q,(0,start))
    distance[start] = 0

    while q:

        dist , now = heapq.heappop(q)


        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]

            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))

    return distance



N, E = map(int,input().split())
graph = [[] for _ in range(N+1)]
for _ in range(E):
    a,b,c = map(int,input().split())

    graph[a].append((b,c))
    graph[b].append((a,c))

v1, v2 = map(int,input().split())

d0 = solution(1)
d1 = solution(v1)
d2 = solution(v2)

answer = min(d0[v1] + d1[v2] + d2[N], d0[v2] + d2[v1] + d1[N])

if answer >= INF:
    print(-1)
else:
    print(answer)

    








