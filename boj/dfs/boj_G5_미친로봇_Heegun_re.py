"""https://www.acmicpc.net/problem/1405"""


"""미친 로봇"""



N_, E, W, S, N = map(int,input().split())

p = [E/100, W/100, S/100, N/100]
d =[(0,1),(0,-1),(1,0),(-1,0)]

result = 0

visited = [(0,0)]

def dfs(y, x, n, per, visited):
    global result
    #print(n)
    if n == 0:
        result += per
        return

    for i in range(4):
        ny = y+d[i][0]
        nx = x+d[i][1]
        if (ny,nx) not in visited:
            visited.append((ny,nx))
            dfs(ny, nx, n-1, per*p[i], visited)
            #print(visited)
            visited.pop()

dfs(0, 0, N_, 1, visited)
print(result)