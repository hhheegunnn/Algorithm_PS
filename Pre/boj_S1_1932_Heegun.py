"""https://www.acmicpc.net/problem/1932"""


"""정수 삼각형"""

# git add week_09_10/boj_S1_1932_Heegun.py
# git commit -m "[김희건] boj 정수 삼각형"


def solution(graph,n):


    for i in range(1,len(graph)):
        for j in range(i+1):
            if j == 0:
                graph[i][j] += graph[i-1][j]

            elif j == len(graph[i])-1:
                graph[i][j] += graph[i-1][j-1]
                
            else:
                graph[i][j] += max(graph[i-1][j], graph[i-1][j-1])

    return max(graph[n-1])


N = int(input())
Graph = []
for _ in range(N):
    tmp = list(map(int,input().split()))
    Graph.append(tmp)

print(solution(Graph,N))




