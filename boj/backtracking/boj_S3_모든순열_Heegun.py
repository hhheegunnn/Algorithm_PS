"""https://www.acmicpc.net/problem/10974"""


"""
from itertools import permutations


N = int(input())

k = list(permutations(range(1,N+1),N))

print(k)
"""

N = int(input())
visited = [False for _ in range(N+1)]
result = []

def dfs(length):

    if length == N:
        print(*result)
        return

    for i in range(1,N+1):
        if not visited[i]:
            result.append(i)
            visited[i] = True

            dfs(length+1)

            result.pop()
            visited[i] = False

dfs(0)

