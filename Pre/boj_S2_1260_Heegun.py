"""https://www.acmicpc.net/problem/1260"""



"""DFS와 BFS"""


# git add week_05/boj_S2_1260_Heegun.py

# git commit -m "[김희건] boj DFS와 BFS"

from collections import deque

N , M , start = map(int,input().split())

graph = [[] for _ in range(N+1)]


for _ in range(M):
    s,e = map(int,input().split())

    graph[s].append(e)
    graph[e].append(s)
    graph[s].sort()
    graph[e].sort()


#print(graph)

visited_dfs = []
visited_bfs = []
q = deque()

def dfs_recursive(graph, start, visited):
    visited.append(start)

    for i in graph[start]:
        if i not in visited:
            dfs_recursive(graph, i, visited)
    
    return visited

def bfs(graph,start,visited_bfs):
    q.append(start)

    while q:
        tmp = q.popleft()
        if tmp not in visited_bfs:
            visited_bfs.append(tmp)
            q.extend(graph[tmp])
        else:
            continue
    return visited_bfs




print(*dfs_recursive(graph, start, visited_dfs))
print(*bfs(graph, start, visited_bfs))








