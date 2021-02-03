"""https://www.acmicpc.net/problem/1922"""


"""네트워크 연결"""

# git add week_12/boj_G4_1922_Heegun.py
# git commit -m "[김희건] boj 네트워크 연결 [최소 신장 트리 (크루스칼) 기본]"


def find_parent(parent,x):

    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])

    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a < b :
        parent[b] = a
    else:
        parent[a] = b

v = int(input())
e = int(input())
parent = [0] * (v+1)

edges = []

result = 0

for i in range(1,v+1):
    parent[i] = i

for _ in range(e):
    a, b, cost = map(int,input().split())

    edges.append((cost,a,b))

edges.sort()

for edge in edges:
    cost , a, b = edge

    if find_parent(parent,a) != find_parent(parent,b):
        union_parent(parent,a,b)
        result += cost
print(result)
