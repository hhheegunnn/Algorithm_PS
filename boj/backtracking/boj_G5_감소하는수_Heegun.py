"""https://www.acmicpc.net/problem/1038"""

import sys

N = int(input())



result = []
cnt = 0

def dfs(length,tmp,NN):

    global cnt
        

    if len(result) == length:
        if cnt == NN:
            print(''.join(map(str,result)))
            sys.exit()
        cnt += 1
        return

    for i in range(tmp):
        if not visited[i]:
            visited[i] = True
            result.append(i)

            dfs(length,result[-1],NN)

            visited[i] = False
            result.pop()


if N <= 9:
    print(N)
elif N >= 1023:
    print(-1)
else:
    NN = N-10
    visited = [False for _ in range(10)]
    length = 1
    while True:
        length += 1
        dfs(length,10,NN)
