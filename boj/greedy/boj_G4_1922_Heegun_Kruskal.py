"""https://www.acmicpc.net/problem/1922"""


"""네트워크 연결"""


N = int(input())

M = int(input())


graph = []

for _ in range(M):

    a,b,c = map(int,input().split())

    graph.append([a,b,c])

graph.sort(key=lambda x: x[2])

parent = [i for i in range(N+1)]

result = 0

def find_parent(parent,x):

    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])

    return parent[x]


def union_parent(parent,x,y):

    a = find_parent(parent,x)
    b = find_parent(parent,y)

    if a > b:
        parent[a] = b
    else:
        parent[b] = a
    


for edge in graph:

    a,b,cost = edge
    #a와 b는 한 집합에 이미 속해있음

    #부모가 찾고 다르면 합집합
    if find_parent(parent,a) != find_parent(parent,b):
        union_parent(parent,a,b)
        result += cost


print(result)

