"""https://www.acmicpc.net/problem/1766"""


""" 문제집 """

# git add week_12/boj_G2_1766_Heegun.py
# git commit -m "[김희건] boj 문제집 [위상정렬 + 우선순위큐]"

#from collections import deque
import heapq

v,e = map(int,input().split())

indegree = [0] *(v+1)

graph = [[] for i in range(v+1)]

for _ in range(e):
    a,b = map(int,input().split())
    graph[a].append(b)
    indegree[b] += 1


def topology_sort():
    result = []
    q = []
    #print(indegree)
    for i in range(1,v+1):
        if indegree[i] == 0:
            heapq.heappush(q,i)
            

    while q:
        now = heapq.heappop(q)
        #print(now)
        result.append(now)
        for i in graph[now]:
            indegree[i] -= 1

            if indegree[i] == 0:
                heapq.heappush(q,i)

    return result

a = topology_sort()

print(*a)