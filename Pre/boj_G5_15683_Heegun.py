"""https://www.acmicpc.net/problem/15683"""


"""감시"""

# 4: 30 ~ 6 : 30

# git add boj_implementation/G/G5/15683/boj_G5_15683_Heegun.py
# git commit -m "[김희건] boj 감시 [비효율적, bfs으로 다시 해보기]"

from itertools import product
import copy

cnt = 0
cccnt = 0
def cctv_1(board, d, r_1, c_1):
    global cnt
    if d == 1:
        for c in range(c_1+1,M):
            if board[r_1][c] == 6:
                break
            elif board[r_1][c] == 0:
                board[r_1][c] = -1
                cnt += 1
            else:
                continue

    elif d == 2:
        for r in range(r_1+1,N):
            if board[r][c_1] == 6:
                break
            elif board[r][c_1] == 0:
                board[r][c_1] = -1
                cnt += 1
            else:
                continue

    elif d == 3:
        for c in range(c_1-1,-1,-1):
            if board[r_1][c] == 6:
                break
            elif board[r_1][c] == 0:
                board[r_1][c] = -1
                cnt += 1
            else:
                continue

    else:
        for r in range(r_1-1,-1,-1):
            if board[r][c_1] == 6:
                break
            elif board[r][c_1] == 0:
                board[r][c_1] = -1
                cnt += 1
            else:
                continue

def cctv_2(board, d, r_2, c_2):
    if d == 1:
        cctv_1(board,1,r_2,c_2)
        cctv_1(board,3,r_2,c_2)
    else:
        cctv_1(board,2,r_2,c_2)
        cctv_1(board,4,r_2,c_2)

def cctv_3(board, d, r_3, c_3):
    if d == 1:
        cctv_1(board,1,r_3,c_3)
        cctv_1(board,4,r_3,c_3)
    elif d == 2:
        cctv_1(board,1,r_3,c_3)
        cctv_1(board,2,r_3,c_3)
    elif d == 3:
        cctv_1(board,3,r_3,c_3)
        cctv_1(board,2,r_3,c_3)
    else:
        cctv_1(board,3,r_3,c_3)
        cctv_1(board,4,r_3,c_3)

def cctv_4(board, d, r_4, c_4):
    if d == 1:
        cctv_3(board, 1, r_4, c_4)
        cctv_1(board, 3, r_4, c_4)
    elif d == 2:
        cctv_3(board, 2, r_4, c_4)
        cctv_1(board, 4, r_4, c_4)
    elif d == 3:
        cctv_3(board, 3, r_4, c_4)
        cctv_1(board, 1, r_4, c_4)
    else:
        cctv_3(board, 4, r_4, c_4)
        cctv_1(board, 2, r_4, c_4)

def cctv_5(board, d, r_5, c_5):
    cctv_4(board, 1, r_5, c_5)
    cctv_1(board, 2, r_5,c_5)

def combi_cctv(board):

    global cccnt

    result = []

    for r in range(N):
        for c in range(M):
            tmp = board[r][c]
            if board[r][c] == 6:
                cccnt += 1

            k = []
            if tmp in [1,2,3,4,5]:
                if tmp == 1 or tmp == 3 or tmp == 4:
                    for i in range(1,5):
                        k.append([tmp,i,r,c])
                if tmp == 2:
                    for i in range(1,3):
                        k.append([tmp,i,r,c])
                if tmp == 5:
                    k.append([tmp,1,r,c])
                result.append(k)
    
    return list(product(*result))

def solution(bboard,n,m):

    #board = copy.deepcopy(bboard)

    global cnt
    global cccnt

    cctv_list = combi_cctv(bboard)
    
    cnt_list = []

    

    for l in cctv_list:
        board = copy.deepcopy(bboard)
        ccnt = len(l)
        for cctv in l:
            cctv_num = cctv[0]
            cctv_d = cctv[1]
            cctv_r = cctv[2]
            cctv_c = cctv[3]

            if cctv_num == 1:
                cctv_1(board, cctv_d , cctv_r, cctv_c)
            elif cctv_num == 2:
                cctv_2(board, cctv_d , cctv_r, cctv_c)
            elif cctv_num == 3:
                cctv_3(board, cctv_d , cctv_r, cctv_c)
            elif cctv_num == 4:
                cctv_4(board, cctv_d , cctv_r, cctv_c)
            else:
                cctv_5(board, cctv_d , cctv_r, cctv_c)
        
        cnt_list.append(cnt)
        cnt = 0
        

    return n*m - (max(cnt_list) + ccnt + cccnt)





N, M = map(int,input().split())
# N y r     # M x c

Board = [list(map(int,input().split())) for _ in range(N)]

print(solution(Board,N,M))

