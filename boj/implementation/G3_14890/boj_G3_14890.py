"""https://www.acmicpc.net/problem/14890"""


"""경사로"""


def road(L,r):

    check = [0 for _ in range(N)]

    for c in range(N-1):
        if abs(board[r][c] - board[r][c+1]) >1 :
            return 0
        
        if board[r][c] < board[r][c+1]:
            tmp = [0 for _ in range(N)]
            for l in range(L):
                if c - l < 0:
                    return 0
                if board[r][c] != board[r][c-l] or check[c-l] != 0:
                    return 0
                tmp[c-l] = 1
            check = tmp

        elif board[r][c] > board[r][c+1]:
            tmp = [0 for _ in range(N)]
            for l in range(L):
                if c+l+1 >= N:
                    return 0
                if board[r][c+1] != board[r][c+l+1] or check[c+l+1] != 0:
                    return 0
                tmp[c+l+1] = 1
            check = tmp
        
    return 1





N,L = map(int,input().split())

board = [list(map(int,input().split())) for _ in range(N)]

result = 0

for r in range(N):
    result += road(L,r)

board = list(map(list,zip(*board)))

for r in range(N):
    result += road(L,r)

print(result)

