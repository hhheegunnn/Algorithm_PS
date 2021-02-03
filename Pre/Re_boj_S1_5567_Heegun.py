"""https://www.acmicpc.net/problem/5567"""


""" 결혼식"""

# git add boj_implementation/S/S1/5567/Re_boj_S1_5567_Heegun.py
# git commit -m "[김희건] boj 결혼식 [dfs 응용]"



from collections import defaultdict



n = int(input())

m = int(input())

graph = defaultdict(list)

for _ in range(m):
    s,e = map(int,input().split())

    graph[s].append(e)
    graph[e].append(s)


visited = [0 for _ in range(n+1)]

result =[]

def dfs(graph,start,visited,cnt):

    if cnt == 3:
        return

    
    if visited[start] == 0:
        visited[start]= 1
        result.append(start)

    for i in graph[start]:
        dfs(graph,i,visited,cnt+1)

dfs(graph,1,visited,0)
print(len(result)-1)
#print(visited)







