"""https://programmers.co.kr/learn/courses/30/lessons/49189"""


"""가장 먼 노드"""

# git add week_12/pg_Lv3_49189_Heegun.py
# git commit -m "[김희건] pg 가장 먼 노드"

import sys
import heapq

INF = sys.maxsize

def solution(n,vertex):


    graph = [[] for _ in range(n+1)]
    distance = [INF] * (n+1)

    for i in vertex:
        s = i[0]
        e = i[1]

        graph[s].append(e)
        graph[e].append(s)

    
    q = []
    heapq.heappush(q,(0,1))
    distance[1] = 0

    while q:

        dist , now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = 1 + dist

            if cost < distance[i]:
                distance[i] = cost
                heapq.heappush(q,(cost,i))

    #print(distance)
    cnt = 0
    max_cost = max(distance[1:n+1])
    #print(max_cost)

    for i in range(1,n+1):
        if distance[i] == max_cost:
            cnt += 1

        

    #print(cnt)
    return cnt


    

    




solution(6,[[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]	)
        
