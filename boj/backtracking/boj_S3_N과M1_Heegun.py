"""https://www.acmicpc.net/problem/15649"""


"""N과 M1"""



N, M = map(int,input().split())

visited = [False for _ in range(N+1)]
result = []

def dfs(x):

    if x == M:
        print(*result)
        return

    for i in range(1,N+1):
        if not visited[i]:
            visited[i] = True
            result.append(i)
            
            dfs(x+1)

            visited[i]=False
            result.pop()

dfs(0)




