from collections import defaultdict

skills = list(map(str,input().split()))
k = len(skills)

n = int(input())


# 후행 스킬
adj = [[] for _ in range(k)]

# 선행스킬의 갯수 -> 0 이면 단독스킬
ind = [0 for _ in range(k)]


# 스킬을 인덱스 번호로
def conv(skill_name):
    return skills.index(skill_name)

for _ in range(n):
    s,e = map(str,input().split())
    s,e = conv(s),conv(e)
    adj[s].append(e)
    ind[e] += 1

def dfs(idx,path):

    if len(adj[idx]) == 0:
        print(' '.join(path))
        return
    for nxt in adj[idx]:
        dfs(nxt,path+[skills[nxt]])
    

for i in range(k):
    if ind[i] == 0:
        dfs(i,[skills[i]])




