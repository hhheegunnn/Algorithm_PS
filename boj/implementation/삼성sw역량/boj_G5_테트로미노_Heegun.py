"""https://www.acmicpc.net/problem/14500"""



"""테트로미노"""




N, M = map(int,input().split())


board = [list(map(int,input().split())) for _ in range(N)]



result_1 = []

def find_max_1(r,c):
    tmp = board[r][c] + board[r][c+1] + board[r][c+2]
    mx = 0

    if 0<= r-1 < N:
        mx = max(mx, board[r-1][c], board[r-1][c+1], board[r-1][c+2])
    if 0<= c+3 < M:
        mx = max(mx, board[r][c+3])
    if 0<= r+1 < N:
        mx = max(mx, board[r+1][c], board[r+1][c+1], board[r+1][c+2])
    return mx+tmp

def find_max_2(r,c):
    tmp = board[r][c] + board[r+1][c] + board[r+2][c]
    mx = 0

    if 0<= c-1 < M:
        mx = max(mx, board[r][c-1], board[r+1][c-1], board[r+2][c-1])
    if 0<= r+3 < N:
        mx = max(mx, board[r+3][c])
    if 0<= c+1 < M:
        mx = max(mx, board[r][c+1], board[r+1][c+1], board[r+2][c+1])
    return mx+tmp

def find_max_3(r,c):

    tmp = board[r][c] + board[r+1][c] + board[r+1][c+1]
    mx = 0

    if 0<= c-1 < M:
        mx = max(mx, board[r][c-1])
    if 0<= r+2 < N:
        mx = max(mx,board[r+2][c+1])
    return mx+tmp

def find_max_4(r,c):

    tmp = board[r][c] + board[r][c+1] + board[r+1][c]
    mx = 0

    if 0<= c-1 < M:
        mx = max(mx, board[r+1][c-1])
    if 0<= r-1 < N:
        mx = max(mx,board[r-1][c+1])
    return mx+tmp




def solution(board):
    mx_result = 0

    for r in range(N):
        for c in range(M):

            if 0<= c+2 < M:
                mx_result = max(mx_result, find_max_1(r,c))
            
            if 0<= r+2 < N:
                mx_result = max(mx_result, find_max_2(r,c))

            if 0<= r+1 < N and 0<= c+1 < M:
                tmp = board[r][c] + board[r+1][c+1] + board[r+1][c] + board[r][c+1]
                mx_result = max(mx_result, tmp)

            if 0<= r+1 < N and 0<= c+1 < M :
                mx_result = max(mx_result, find_max_3(r,c))
                mx_result = max(mx_result, find_max_4(r,c))


    
    return mx_result

print(solution(board))

