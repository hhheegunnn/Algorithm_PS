"""https://www.acmicpc.net/problem/16234"""


""" 인구 이동 """

# git add boj_implementation/G/G5/16234/Re_boj_G5_16234_Heegun.py
# git commit -m "[김희건] boj 인구이동 [python사용]"

from collections import deque

delta = [(1,0),(-1,0),(0,1),(0,-1)]

def check_in(y,x):
    if 0<= y < N and 0<= x < N:
        return True
    else:
        return False

def diff_pop_n(y,x):
    for i in delta:
        ny,nx = y+i[0], x+i[1]
        if check_in(ny,nx):
            if L <= abs(Board[y][x] - Board[ny][nx]) <= R:
                return True
      
    return False


def bfs(start_r, start_c):
    
    start_node = [start_r, start_c]
    q = deque([start_node])
    visited[start_r][start_c] = True
    pop_sum = Board[start_r][start_c]
    nation = [[start_r,start_c]]

    while q:
        node = q.popleft()


        for d in delta:
            node_r = node[0]+d[0]
            node_c = node[1]+d[1]
            
            if check_in(node_r , node_c):
                if not visited[node_r][node_c]:
                    if L <= abs(Board[node[0]][node[1]] - Board[node_r][node_c]) <= R:
                        #print(node_r, node_c)
                        pop_sum += Board[node_r][node_c]
                        nation.append([node_r,node_c])
                        q.append([node_r, node_c])
                        visited[node_r][node_c] = True



    if len(nation) > 1:
        for i in nation:
            naiont_pop = pop_sum//len(nation)
            Board[i[0]][i[1]] = naiont_pop
            nextq.append([i[0],i[1]])
        return True

    elif len(nation) == 1:
        return False
    







N, L, R = map(int,input().split())
Board = [list(map(int,input().split())) for _ in range(N)]
cnt = 0
nextq = deque()


for i in range(N):
    for j in range(N):
        nextq.append([i,j])

while True:

    flag = False

    visited = [[False for _ in range(N)] for _ in range(N)]
    
    size = len(nextq)

    for _ in range(size):
        i,j = nextq.popleft()
        if visited[i][j] or not diff_pop_n(i,j):
            continue
        if bfs(i,j):

            flag= True
    
    if flag:
        cnt += 1
    else:
        print(cnt)
        break




