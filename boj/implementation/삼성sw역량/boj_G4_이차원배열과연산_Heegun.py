"""https://www.acmicpc.net/problem/17140"""

"""이차원배열과 연산"""

from collections import defaultdict

r,c,k = map(int,input().split())

board = [list(map(int,input().split())) for _ in range(3)]


def padding(tmp_board):
    mx = 0

    for i in range(len(tmp_board)):

        mx = max(mx,len(tmp_board[i]))

    for i in range(len(tmp_board)):
        for _ in range(mx - len(tmp_board[i])):
            tmp_board[i].append(0)

    return tmp_board


def func_R(board):
    
    tmp_board = []

    for r in range(len(board)):
        r_tmp = defaultdict(lambda : 0)


        for c in range(len(board[0])):
           
            if board[r][c] != 0:

                r_tmp[board[r][c]] += 1

        t = []
        for num,cnt in sorted(r_tmp.items(), key=lambda x: (x[1],x[0])):
            t.append(num)
            t.append(cnt)
        tmp_board.append(t)
        
    result = padding(tmp_board)

    if len(result[0]) >= 100:

        for r in range(len(result)):
            result[r] = result[r][:100]


    return result



def func_C(board):

    board = list(zip(*board))

    tmp_board = []

    for r in range(len(board)):
        r_tmp = defaultdict(lambda : 0)


        for c in range(len(board[0])):
            
            if board[r][c] != 0:

                r_tmp[board[r][c]] += 1

        t = []
        for num,cnt in sorted(r_tmp.items(), key=lambda x: (x[1],x[0])):
            t.append(num)
            t.append(cnt)
        tmp_board.append(t)
        

    result = padding(tmp_board)

    if len(result[0]) >= 100:

        for r in range(len(result)):
            result[r] = result[r][:100]

    result = list(zip(*result))

    return result





def solution(board):

    sec=0
    
    while True:

        if len(board) > r-1 and len(board[0]) > c-1:
            if board[r-1][c-1] == k:
                return sec

        if sec >= 101:
            return -1

        if len(board) >= len(board[0]):
            board = func_R(board)
        else:
            board = func_C(board)

        sec += 1

    

print(solution(board))