"""https://www.acmicpc.net/problem/2606"""


"""바이러스"""

from collections import defaultdict, deque

N = int(input())
L = int(input())

graph = defaultdict(list)
# 그래프의 key에 해당 값이 없으면 리스트로 초기화

for i in range(L):
    s,e = map(int,input().split())

    graph[s].append(e)
    graph[e].append(s)

#dfs 반복문
start = 1

visited = []
q = deque([start])

while q:

    tmp = q.popleft()
    if tmp not in visited:
        visited.append(tmp)
    else:
        continue

    q.extend(graph[tmp])

print(len(visited)-1)

#dfs 재귀
start = 1
visited = []
q = deque([start])

def dfs(s):
    visited.append(s)
    for i in graph[s]:
        if i not in visited :
            dfs(i)

dfs(start)

print(len(visited)-1)






