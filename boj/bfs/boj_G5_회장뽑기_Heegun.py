"""https://www.acmicpc.net/problem/2660"""


"""회장 뽑기"""

from collections import deque
import sys

N = int(input())

graph = [[] for _ in range(N+1)]

while True:
    a,b = map(int,input().split())
    if a== -1 and b == -1:
        break
    graph[a].append(b)
    graph[b].append(a)

#print(graph)

def bfs(start):

    visited = [False for _ in range(N+1)]

    q = deque([start])
    visited[start] = True
    result = [0 for _ in range(N+1)]

    while q:
        node = q.popleft()

        for i in graph[node]:
            if not visited[i]:
                q.append(i)
                visited[i] = True
                result[i] = result[node] + 1

    return max(result)

r = [0 for _ in range(N+1)]

min_ = sys.maxsize
for i in range(1,N+1):
    m = bfs(i)
    r[i] = m

score = min(r[1:])
candidate = []

for i in range(1,N+1):
    if r[i] == score:
        candidate.append(i)

print(score,len(candidate))
print(*candidate)



    

