"""https://www.acmicpc.net/problem/17471"""


""" 게리맨더링 """

from collections import defaultdict,deque
from itertools import combinations
import sys

N = int(input())

graph = defaultdict(list)

pop_list  = list(map(int,input().split()))
pop_list.insert(0,0)

for i in range(N):

    tmp = list(map(int,input().split()))

    for j in range(1,len(tmp)):
        graph[i+1].append(tmp[j])



def bfs(start,graph,area):

    visited = [False for _ in range(N+1)]

    q = deque([start])
    cnt = 1

    visited[start] = True

    while q:

        s = q.popleft()

        for node in graph[s]:

            if not visited[node] and node in area:
                visited[node] = True
                q.append(node)
                cnt += 1

    if cnt == len(area):
        return True
    else:
        return False



min_diff = sys.maxsize

area_num_list = [i for i in range(1,N+1)]
for i in range(1,N//2+1):
    candidate = combinations(area_num_list,i)
    
    for area_1 in candidate:
        area_1 = list(area_1)
        area_2 = list(set(area_num_list) - set(area_1))

        if bfs(area_1[0],graph,area_1) and bfs(area_2[0],graph,area_2):
            
            pop_area_1 = [pop_list[i] for i in area_1]
            pop_area_2 = [pop_list[i] for i in area_2]
            min_diff = min(min_diff, abs(sum(pop_area_1)- sum(pop_area_2)))

    
if min_diff == sys.maxsize:
    print(-1)
else:
    print(min_diff)






