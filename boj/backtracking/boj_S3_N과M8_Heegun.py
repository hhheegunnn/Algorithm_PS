"""https://www.acmicpc.net/problem/15657"""



N,M = map(int,input().split())

numbers = list(map(int,input().split()))
numbers.sort()

result = []

def dfs(length,idx):

    if length == M :
        print(*result)
        return


    for i in range(idx,len(numbers)):

        result.append(numbers[i])

        dfs(length+1, i)

        result.pop()

dfs(0,0)

