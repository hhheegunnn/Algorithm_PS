"""https://www.acmicpc.net/problem/17140"""


"""이차원 배열과 연산 """

# git add boj_implementation/G/G4/17140/boj_G4_17140_Heegun.py
# git commit -m "[김희건] boj 이차원 배열과 연산 [Counter, zip]"

from collections import Counter

def func(R,C):

    for index in range(len(board)):
        tmp = []
        a = board[index]
        b = list(Counter(a).items())
        b.sort(key = lambda x: (x[1],x[0]))
        for i in range(len(b)):
            tmp += [j for j in b[i] if b[i][0] != 0]
        board[index] = tmp

    max_R = max(len(i) for i in board)

    for i in range(len(board)):
        if len(board[i]) < max_R:
            while len(board[i]) != max_R:
                board[i].append(0)


def swap_RC(b):
    return list(map(list,zip(*b)))


r,c,k = map(int,input().split())

board = [list(map(int,input().split())) for _ in range(3)]


cnt = 0
#print(board)

while True:

    board_r = len(board)
    board_c = len(board[0])

    if board_r >= 100:
        board = board[:100]
    if board_c >= 100:
        for i in range(board_r):
            board[i] = board[i][:100]


    if r <= board_r and c <= board_c:
        if board[r-1][c-1] == k:
            #print(board)
            print(cnt)
            break


    if board_r >= board_c:
        func(board_r,board_c)
        #print(board)
    else:
        board = swap_RC(board)
        #print(board)
        func(board_r,board_c)
        #print(board)
        board = swap_RC(board)

    cnt += 1

    if cnt > 100:
        print(-1)
        break

    #print(board)
    



