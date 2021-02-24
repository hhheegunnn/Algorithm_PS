# 크루스칼(최소 스패닝 트리)


def find_parent(parent,x):

    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])

    return parent[x]

def union_parent(parnet,a,b):

    a = find_parent(parent,a)
    b = find_parent(parent,b)

    if a > b:
        parent[a] = b
    else:
        parent[b] = a 

v , e = map(int,input().split())

graph = []

for i in range(e):
    a,b,c = map(int,input().split())

    graph.append([a,b,c])

graph.sort(key=lambda x: x[2])
#print(graph)

parent = [i for i in range(v+1)]
result = 0
#print(parent)

for edge in graph:

    a,b, cost = edge

    if find_parent(parent,a) != find_parent(parent,b):
        union_parent(parent,a,b)
        result += cost


print(result)


    


