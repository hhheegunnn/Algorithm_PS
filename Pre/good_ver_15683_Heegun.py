

delta = [(0,1),(0,-1),(1,0),(-1,0)]
direction = {1:[[0],[1],[2],[3]], 2:[[0,1], [2,3]], 3: [[0,2],[1,3],[0,3],[1,2]], 4: [[0,1,2], [1,2,3],[2,3,0],[3,0,1]], 5:[[0,1,2,3]]}


def dfs(n, arr):
    global min_ans
    if n == len(camera):
        visited = [[False for _ in range(M)] for _ in range(N)]
        for idx, c in enumerate(camera):
            x = c[0]
            y = c[1]
            for element in arr[idx]:
                c = 1
                while True:
                    nx = x + delta[element][0]*c
                    ny = y + delta[element][1]*c
                    if 0<=nx<N and 0<=ny<M and office[nx][ny] !=6:
                        if office[nx][ny]==0 and visited[nx][ny] == False:
                            visited[nx][ny] = True
                        c+=1
                    else:
                        break
        cnt = 0
        for ii in range(N):
            for jj in range(M):
                if board[ii][jj] == 0 and visited[ii][jj] == False:
                    cnt +=1
        if min_sq > cnt:
            min_sq = cnt
        return

    for ele in direction[board[camera[n][0]][camera[n][1]]]:
        arr.append(ele)
        dfs(n+1, arr)
        arr.pop()




N, M = map(int,input().split())
# N y r     # M x c

board = [list(map(int,input().split())) for _ in range(N)]

camera = []
min_ans = 0

for i in range(N):
    for j in range(M):
        if 1<=board[i][j]<=5:
            camera.append((i,j))
        if office[i][j] == 0:
            min_ans +=1

dfs(0,[])
print(min_ans)
