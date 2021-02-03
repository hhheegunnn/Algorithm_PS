"""https://programmers.co.kr/learn/courses/30/lessons/43162"""

"""네트워크"""

# git add week_06/pg_Lv3_43162_Heegun.py
# git commit -m "[김희건] pg 네트워크 [dfs]"

from collections import defaultdict

def dfs(start,visited,computers):
    visited[start] = True

    for i in range(len(computers)):

        if not visited[i] and computers[start][i] == 1:
            dfs(i,visited,computers)



def solution(n, computers):

    visited = [False]*(n)

    cnt = 0

    for i in range(n):
        if not visited[i]:
            dfs(i,visited,computers)
            cnt += 1
        else:
            continue

    return cnt


    
