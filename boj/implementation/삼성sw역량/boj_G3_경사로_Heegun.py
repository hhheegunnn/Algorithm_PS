"""https://www.acmicpc.net/problem/14890"""


"""경사로"""


N, L = map(int,input().split())

board = [list(map(int,input().split())) for _ in range(N)]

def solution(board):

    result = 0

    for r in range(N):
        for c in range(N-1):
            if board[r][c] == board[r][c+1]:
                


            


    board = list(map(list,zip(*board)))

    for r in range(N):
        for c in range(N):
            pass

    return result

print(solution(board))
