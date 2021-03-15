"""https://programmers.co.kr/learn/courses/30/lessons/43164"""


"""여행경로"""

from collections import defaultdict

def solution(tickets):
    
    graph = defaultdict(list)

    for t in tickets:
        graph[t[0]].append(t[1])

    for c in graph:
        graph[c].sort()


    def dfs(start,result):

        if len(result) == cnt:
            return result


        for idx, c in enumerate(graph[start]):
            graph[start].pop(idx)

            r = result[:]
            r.append(c)

            ret = dfs(c,r)

            if ret:
                return ret

            graph[start].insert(idx,c)



    

    result = ["ICN"]
    cnt = len(tickets) + 1
    answer = dfs("ICN",result)
    
    return answer

"""
from collections import defaultdict
def solution(tickets):
    # 특정 티켓의 인접 리스트를 구하는 함수
    def init_graph():
        routes = defaultdict(list)
        for key, value in tickets:
            routes[key].append(value)
        return routes

    # 스택을 사용한 DFS
    def dfs():
        stack = ["ICN"]
        path = []  # 가려고하는 경로를 저장하는 변수
        while len(stack) > 0:  # stack이 비어있을 때까지
            top = stack[-1]
            # 특정 공항에서 출발하는 표가 없다면 또는 있지만 티켓을 다 써버린 경우
            if top not in routes or len(routes[top]) == 0:
                path.append(stack.pop())
            else:
                stack.append(routes[top].pop(0))
        return path[::-1]

    routes = init_graph()
    for r in routes:
        routes[r].sort()

    answer = dfs()
    return answer
"""

#print(solution([["ICN", "A"], ["A", "C"], ["A", "D"], ["D", "B"], ["B", "A"]]))
print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]))