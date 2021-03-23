"""https://www.acmicpc.net/problem/15654"""




N,M = map(int,input().split())

numbers = list(map(int,input().split()))


numbers.sort()

visited = [False for _ in range(len(numbers))]

result =[]

def dfs(length):

    if length == M :
        print(*result)
        return 


    for i in range(len(numbers)):

        if not visited[i]:
            result.append(numbers[i])
            visited[i]= True
            dfs(length+1)

            visited[i] = False
            result.pop()

dfs(0)
