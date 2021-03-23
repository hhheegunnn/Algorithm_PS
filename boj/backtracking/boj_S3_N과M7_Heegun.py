"""https://www.acmicpc.net/problem/15656"""




N, M = map(int,input().split())

numbers = list(map(int,input().split()))
numbers.sort()

result = []


def dfs(length):

    if length == M :
        print(*result)
        return 

    for i in range(len(numbers)):

        result.append(numbers[i])

        dfs(length+1)

        result.pop()

dfs(0)
