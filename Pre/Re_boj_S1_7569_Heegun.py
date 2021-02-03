"""https://www.acmicpc.net/problem/7569"""


""" 토마토 """


# git add week_05/Re_boj_S1_7569_Heegun.py
# git commit -m "[김희건] boj 토마토"


from collections import deque
import sys

dir_h = [1,-1,0,0,0,0]
dir_r = [0,0,0,-1,0,1]
dir_c = [0,0,-1,0,1,0]


c,r,h = map(int,input().split())


board = [[] for _ in range(h)]
q = deque()

for i in range(h):
    for _ in range(r):
        tmp = list(map(int,input().split()))
        board[i].append(tmp)

visited = [[[0]*c for _ in range(r)] for _ in range(h)]

def check_in(H,R,C):
    if 0<=H<h and 0<=R<r and 0<=C<c:
        return True
    else:
        return False

def bfs():

    while q:
        H,R,C = q.popleft()
        for i in range(6):
            nH = H + dir_h[i]
            nR = R + dir_r[i]
            nC = C + dir_c[i]

            if check_in(nH,nR,nC) and board[nH][nR][nC] == 0 and visited[nH][nR][nC] == 0:
                q.append([nH,nR,nC])
                board[nH][nR][nC] = 1
                visited[nH][nR][nC] = visited[H][R][C] + 1


for i in range(h):
    for j in range(r):
        for k in range(c):
            if board[i][j][k] == 1 and visited[i][j][k] == 0:
                q.append([i,j,k])
                visited[i][j][k] = 1
bfs()

                

for a in board:
    for i in a:
        if 0 in i:
            print(-1)
            sys.exit()
cnt = 0
for i in visited:
    for j in i:
        v_max = max(j)
        cnt = max(cnt,v_max)
#print(visited)
print(cnt-1)


