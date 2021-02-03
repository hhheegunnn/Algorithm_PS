"""https://programmers.co.kr/learn/coaurses/30/lessons/43105"""

"""정수 삼각형"""


# git add week_11/pg_lv3_43105_Heegun.py
# git commit -m "[김희건] pg 정수 삼각형"


def solution(graph):


    for i in range(1,len(graph)):
        for j in range(i+1):
            if j == 0:
                graph[i][j] += graph[i-1][j]

            elif j == len(graph[i])-1:
                graph[i][j] += graph[i-1][j-1]
                
            else:
                graph[i][j] += max(graph[i-1][j], graph[i-1][j-1])

    return max(graph[-1])


Graph = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]

print(solution(Graph))




