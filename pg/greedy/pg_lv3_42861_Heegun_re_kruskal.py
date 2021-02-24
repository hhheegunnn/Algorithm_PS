"""https://programmers.co.kr/learn/courses/30/lessons/42861"""


"""섬 연결하기"""

# 크루스칼 알고리즘 (greedy를 기반으로한 최소 신장 트리 알고리즘)

def find_parent(parent,x):

    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])

    return parent[x]

def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


def solution(n,cost):

    parent = [i for i in range(n)]
    cost.sort(key=lambda x: x[2])
    result = 0

    for edge in cost:
        a,b,cost = edge

        if find_parent(parent,a) != find_parent(parent,b):
            union_parent(parent,a,b)
            result += cost
        #print(parent)
    return result


print(solution(4,[[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]))
    





