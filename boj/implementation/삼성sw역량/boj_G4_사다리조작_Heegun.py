"""https://www.acmicpc.net/problem/15684"""


"""사다리 조작"""





N, M, H = map(int,input().split())

board = [[0 for i in range(N)] for _ in range(H)]

INF = 1e9

for _ in range(M):
    i,j = map(int,input().split())

    board[i-1][j-1] = 1

#print(board)

def check(board):

    for start in range(N):
        c = start

        for r in range(H):
            if board[r][c] == 1:
                c += 1
            elif c > 0 and board[r][c-1] == 1:
                c -= 1
        if start != c:
            return False
    
    return True

ans =4 
def solution(cnt, r, c):
    global ans

    if check(board):
        ans = min(ans,cnt)
        return
    elif cnt== 3 or ans <= cnt:
        return

    for i in range(r,H):

        for j in range(N-1):

            if board[i][j]==1:
                continue
            if j+1 < N and board[i][j+1]==1:
                continue
            if j-1 > 0 and board[i][j-1]==1:
                continue

            board[i][j] = 1
            solution(cnt+1,i,j+2)
            board[i][j] = 0

    

solution(0,0,0)

if ans >= 4:
    print(-1)
else:
    print(ans)


