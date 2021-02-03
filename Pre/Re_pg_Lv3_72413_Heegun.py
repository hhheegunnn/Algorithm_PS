"""https://programmers.co.kr/learn/courses/30/lessons/72413"""


""" 합승 택시 요금 """

# git add week_13/Re_pg_Lv3_72413_Heegun.py
# git commit -m "[김희건] pg 합승 택시 요금"



import sys
import heapq

INF = sys.maxsize

def solution(n,s,a,b,fares):
    graph = [[] for i in range(n+1)]

    for c,d,f in fares:
        graph[c].append((d,f))
        graph[d].append((c,f))


    # 각자 타고 갈때
    cost = dijkstra(n,s,a,graph) + dijkstra(n,s,b,graph)


    for i in range(1,n+1):
        if s != i:
            cost = min(cost, dijkstra(n,s,i,graph) + dijkstra(n,i,a,graph) + dijkstra(n,i,b,graph))
        
    return cost

def dijkstra(n,start,end,graph):

    q = []

    distance = [INF] * (n+1)

    distance[start] = 0
    heapq.heappush(q,(0,start))
    

    while q:

        dist,now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))

    return distance[end]

solution(6,4,6,2,[[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]])
