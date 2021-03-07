"""https://www.acmicpc.net/problem/14719"""


"""빗물"""



H, W = map(int,input().split())

board = list(map(int,input().split()))

result = 0
"""
for _ in range(H):
    tmp = 0
    wall_start = False
    #wall_end = False
    for i in range(W):
        if board[i] != 0:
            if not wall_start:
                wall_start = True
            else:
                result += tmp
                tmp = 0
        else:
            if wall_start:
                tmp += 1
        
    for j in range(W):
        if board[j] > 0 :
            board[j] -= 1
        
    #print(board)

print(result)
"""
def solution(board):
    cnt = 0

    for i in range(W):
        left_max = max(board[:i+1])
        right_max = max(board[i:])

        if board[i] >= min(left_max,right_max):
            continue
        else:
            cnt += min(left_max,right_max) - board[i]

    return cnt

print(solution(board))