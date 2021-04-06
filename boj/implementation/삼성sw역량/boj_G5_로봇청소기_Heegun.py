"""https://www.acmicpc.net/problem/14503"""



"""로봇청소기"""


######
N, M = map(int,input().split())

sr,sc, d = map(int,input().split())

board = [list(map(int,input().split())) for _ in range(N)]
######



def solution(board,sr,sc,d):

    direction = [(-1,0),(0,1),(1,0),(0,-1)]

    cnt = 0
    visited = [[False for _ in range(M)] for _ in range(N)]

    while True:

        # step 1
        if visited[sr][sc] == False:
            visited[sr][sc] = True
            cnt += 1 

        # step2
        clean_flag = False
        for _ in range(4):
            tmp_d = (d + 3)%4
            
            if 0<= sr+direction[tmp_d][0] < N and 0<= sc+direction[tmp_d][1] < M:
                if board[sr+direction[tmp_d][0]][sc+direction[tmp_d][1]] == 0 and not visited[sr+direction[tmp_d][0]][sc+direction[tmp_d][1]]:
                    #print(tmp_d)
                    sr += direction[tmp_d][0]
                    sc += direction[tmp_d][1]
                    d = tmp_d
                    clean_flag = True
                    break
            d = tmp_d
        
        if clean_flag:
            continue
        else:
            # 후진
            if 0<= sr-direction[d][0] < N and 0<= sc-direction[d][1] < M:
                if board[sr-direction[d][0]][sc-direction[d][1]] == 0:
                    sr -= direction[d][0]
                    sc -= direction[d][1]
                else:
                    return cnt
            else:
                return cnt


print(solution(board,sr,sc,d))

"""



# 북동남서
dx = [-1,0,1,0]
dy = [0,1,0,-1]
N, M = map(int,input().split())

r,c,d = map(int,input().split())


board = [list(map(int,input().split())) for _ in range(N)]

ans = 0


def clean(r,c,d):
    global ans
    if board[r][c] == 0:
        board[r][c] = 2
        ans += 1
    for _ in range(4):
        nd = (d+3)%4
        nr = r + dx[nd]
        nc = c + dy[nd]
        if board[nr][nc] == 0:
            clean(nr,nc,nd)
            return
        d = nd
    
    nd = (d+2) %4
    nr = r + dx[nd]
    nc = c + dy[nd]
    if board[nr][nc] == 1:
        return
    clean(nr,nc,d)

clean(r,c,d)
print(ans)

"""




            








