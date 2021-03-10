"""https://programmers.co.kr/learn/courses/30/lessons/43162"""


"""네트워크"""


def dfs(start,computers,visited):

    visited[start] = True

    for i in range(len(computers[start])):
        #print(visited)
        if not visited[i] and computers[start][i] != 0:
            dfs(i,computers,visited)




def solution(n,computers):
    result = 0

    visited = [False for _ in range(n)]

    for i in range(n):
        if not visited[i]:
            #print(visited)
            dfs(i,computers,visited)
            result += 1

    return result

solution(3,[[1, 1, 0], [1, 1, 1], [0, 1, 1]])
solution(3,[[1, 1, 0], [1, 1, 0], [0, 0, 1]])