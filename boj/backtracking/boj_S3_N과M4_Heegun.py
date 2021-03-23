"""https://www.acmicpc.net/problem/15652"""





N, M = map(int,input().split())



result = []


def dfs(length,start):

    if length == M:
        print(*result)
        return


    for i in range(start,N+1):

        result.append(i)
        dfs(length+1, i)
        result.pop()


dfs(0,1)