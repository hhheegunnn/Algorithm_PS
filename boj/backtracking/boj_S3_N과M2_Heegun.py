"""https://www.acmicpc.net/problem/15650"""


"""N과M2"""



N,M = map(int,input().split())


visited = [False for _ in range(N+1)]

result = []


def dfs(length,start):
    

    if length == M:
        print(*result)
        return

    for i in range(start,N+1):
        if not visited[i]:
            visited[i] = True
            result.append(i)
            dfs(length+1, i+1)
            visited[i] = False
            result.pop()


dfs(0,1)


