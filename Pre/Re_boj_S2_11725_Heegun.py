"""https://www.acmicpc.net/problem/11725"""



"""트리의 부모 찾기"""


# git add week_05/Re_boj_S2_11725_Heegun.py
# git commit -m "[김희건] boj 트리의 부모 찾기"



from collections import defaultdict
import sys

sys.setrecursionlimit(1000000)

N  = int(input())
graph = defaultdict(list)

for _ in range(N-1):
    s,e = map(int,input().split())

    graph[s].append(e)
    graph[e].append(s)

#print(graph)


parents = [0 for _ in range(N+1)]

def dfs(s):
    for i in graph[s]:
        if parents[i] == 0:
            parents[i] = s
            dfs(i)

        

dfs(1)


for i in parents[2:]:
    print(i)









