"""https://www.acmicpc.net/problem/2636"""


"""치즈"""

# git add boj_implementation/G/G5/2636/Re_boj_G5_2636_Heegun.py
# git commit -m "[김희건] boj 치즈"

from collections import deque


# 총 치즈의 양



def bfs(sr,sc):
    global left
    q = deque([(sr,sc)])
    visited[sr][sc] = True

    while q:
        now = q.popleft()

        for dy,dx in (1,0),(-1,0),(0,1),(0,-1):
            nr = now[0] + dy
            nc = now[1] + dx
            
            if 0<= nr < R and 0<= nc < C and not visited[nr][nc]:
                visited[nr][nc] = True

                if board[nr][nc] == 1:
                    board[nr][nc] = 2
                    left -= 1
                else:
                    q.append([nr,nc])



def delete():
    for i in range(R):
        for j in range(C):
            if board[i][j] == 2:
                board[i][j] = 0


R , C = map(int,input().split())

board = [list(map(int,input().split())) for _ in range(R)]

left = 0

for i in range(R):
    for j in range(C):
        if board[i][j] == 1:
            left += 1

cnt = 0
result = left

while left != 0:
    visited = [[False for _ in range(C)] for _ in range(R)]
    bfs(0,0)

    if left != 0:
        result = left
    
    cnt += 1
    delete()

print(cnt)
print(result)



                
            
        

"""

6 6
0 0 0 0 0 0 
0 1 1 1 0 0 
0 1 1 0 1 0 
0 1 0 0 1 0 
0 1 1 1 0 0 
0 0 0 0 0 0

6 6
0 0 0 0 0 0 
0 1 1 0 1 0 
0 1 1 0 0 0 
0 1 0 1 0 0 
0 1 1 1 0 0 
0 0 0 0 0 0
"""

