"""https://www.acmicpc.net/problem/15655"""




N,M = map(int,input().split())

numbers = list(map(int,input().split()))
visited = [False for _ in range(len(numbers))]

numbers.sort()

result = []


def dfs(length,idx):

    if length == M:
        print(*result)
        return
    
    for i in range(idx,len(numbers)):

        if not visited[i]:

            visited[i] = True
            result.append(numbers[i])

            dfs(length+1, i+1)

            visited[i] = False
            result.pop()


dfs(0,0)


