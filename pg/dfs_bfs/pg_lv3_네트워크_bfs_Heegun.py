"""https://programmers.co.kr/learn/courses/30/lessons/43162"""



"""네트워크"""



from collections import deque



def bfs(start,visited,computers):

    q = deque([start])
    visited[start] = True

    while q:
        node = q.popleft()

        for i in range(len(computers[node])):
            if not visited[i] and computers[node][i] == 1:
                visited[i] = True
                q.append(i)


def solution(n,computers):

    visited = [False for _ in range(n)]
    result = 0

    for i in range(n):
        if not visited[i]:
            bfs(i,visited,computers)
            result += 1

    return result


print(solution(3,[[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
