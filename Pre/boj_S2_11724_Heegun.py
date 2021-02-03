"""https://www.acmicpc.net/problem/11724"""



"""연결 요소의 개수"""

# git add week_04/boj_S2_11724_Heegun.py

# git commit -m "[김희건] boj 연결 요소의 개수 [파이썬 input 사용 시 시간초과]"


from collections import defaultdict

import sys

sys.setrecursionlimit(10**6)

N,M = map(int,input().split())


graph = defaultdict(list)

for _ in range(M):
    #u,v = map(int,input().split())
    u,v = map(int,sys.stdin.readline().split())

    graph[u].append(v)
    graph[v].append(u)

cnt = 0



def dfs(u):
    #global visited
    for i in graph[u]:
        if i not in visited:
            visited.append(i)
            dfs(i)
    
visited = []


for i in range(1,N+1):
    if i not in visited:
        visited.append(i)
        dfs(i)
        cnt += 1
    else:
        continue

print(cnt)
