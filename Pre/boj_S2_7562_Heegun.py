"""https://www.acmicpc.net/problem/7562"""



"""나이트의 이동"""

# git add week_05/boj_S2_7562_Heegun.py
# git commit -m "[김희건] boj 나이트의 이동"

from collections import deque


def check_in(r,c):
    if 0<=r<l and 0<=c<l:
        return True
    else:
        return False

direction_r = [-1,-2,-2,-1,1,2,2,1]
direction_c = [-2,-1,1,2,2,1,-1,-2]

def bfs(sr,sc):
    q = deque()
    q.append([sr,sc])
    board[sr][sc] = 1 
    while q:
        sr,sc = q.popleft()
        if sr == er and sc == ec:
            return board[er][ec] - 1
        for i in range(8):
            nr = sr + direction_r[i]
            nc = sc + direction_c[i]
            if check_in(nr,nc) and board[nr][nc] == 0:
                q.append([nr,nc])
                board[nr][nc] = board[sr][sc] + 1
    
    

for _ in range(int(input())):
    l = int(input())

    board = list([0 for _ in range(l)] for _ in range(l))
    sr, sc = map(int,input().split())
    board[sr][sc] = 1
    er, ec = map(int,input().split())
    cnt = 0
    print(bfs(sr,sc))

    

    



    

