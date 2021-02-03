"""https://www.acmicpc.net/problem/2644"""

"""촌수계산"""

# path
"""week_04/Re_boj_S2_2644_Heegun.py"""
# commit m
"""[김희건] boj 촌수계산 [bfs로 다시 풀어보기]"""

from collections import defaultdict,deque

n = int(input())

s,e = map(int,input().split())

m = int(input())

graph = defaultdict(list)

for _ in range(m):

    a,b = map(int,input().split())

    graph[a].append(b)
    graph[b].append(a)

visited = [s]
#q =deque([s])

cnt = -1

def dfs(start):
    global cnt 

    if cnt > 0:
        return 
    
    if start == e:
        cnt = len(visited)-1
        return 
    
    for n in graph[start]:
        #print(visited)
        if n not in visited:
            visited.append(n)
            dfs(n)
            #print(visited)
            #print(cnt)
            visited.pop()
    return 

dfs(s)

print(cnt)










    


