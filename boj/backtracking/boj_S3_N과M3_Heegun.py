"""https://www.acmicpc.net/problem/15651"""




N, M = map(int,input().split())



result = []

def dfs(length):

    if length == M:
        print(*result)
        return 

    for i in range(1,N+1):
        result.append(i)

        dfs(length+1)

        result.pop()

dfs(0)








