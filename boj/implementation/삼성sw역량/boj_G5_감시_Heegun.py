"""https://www.acmicpc.net/problem/15683"""



"""감시"""

from itertools import product
from copy import deepcopy

###

N, M = map(int,input().split())

board_og = [list(map(int,input().split())) for _ in range(N)]

####

def check_black(board):

    cnt = 0

    for i in range(N):
        for j in range(M):

            if board[i][j] == 0:
                cnt += 1

    return cnt

#####

def find_camera(board):

    camera = []

    for i in range(N):
        for j in range(M):

            if 1<=board[i][j]<6:

                tmp = []

                if board[i][j] == 1:
                    for k in range(4):
                        tmp.append((board[i][j], k, (i,j)))
                elif board[i][j] == 2 :
                    for k in range(2):
                        tmp.append((board[i][j], k, (i,j)))
                elif board[i][j] == 3 :
                    for k in range(4):
                        tmp.append((board[i][j], k, (i,j)))
                elif board[i][j] == 4 :
                    for k in range(4):
                        tmp.append((board[i][j], k, (i,j)))
                else:
                    tmp.append((board[i][j], 0, (i,j)))
            
                camera.append(tmp)

    camera_list = list(product(*camera))

    #print(camera_list)

    return camera_list

#######


def check_see(d,cord,board):
    if d == 0:
        for r in range(cord[0]-1,-1,-1):
            if board[r][cord[1]] == 0:
                board[r][cord[1]] = '#'
            elif board[r][cord[1]] == 6:
                return
    if d == 1:
        for c in range(cord[1]+1,M):
            if board[cord[0]][c] == 0:
                board[cord[0]][c] = '#'
            elif board[cord[0]][c] == 6:
                return
    if d == 2:
        for r in range(cord[0]+1,N):
            if board[r][cord[1]] == 0:
                board[r][cord[1]] = '#'
            elif board[r][cord[1]] == 6:
                return
    if d == 3:
        for c in range(cord[1]-1,-1,-1):
            if board[cord[0]][c] == 0:
                board[cord[0]][c] = '#'
            elif board[cord[0]][c] == 6:
                return

    return

def solution(board_og):

    camera_list= find_camera(board_og)

    mn = N*M
    

    for c_list in camera_list:

        board = deepcopy(board_og)

        for cn, d, cord in c_list:
            #print(cn,d,cord)
            if cn == 1:
                check_see(d,cord,board)
            elif cn == 2:
                if d == 0:
                    check_see(1,cord,board)
                    check_see(3,cord,board)
                else:
                    check_see(0,cord,board)
                    check_see(2,cord,board)
            elif cn == 3:
                if d == 0:
                    check_see(0,cord,board)
                    check_see(1,cord,board)
                elif d == 1:
                    check_see(3,cord,board)
                    check_see(2,cord,board)
                elif d == 2:
                    check_see(3,cord,board)
                    check_see(0,cord,board)
                else:
                    check_see(1,cord,board)
                    check_see(2,cord,board)
            elif cn == 4:
                if d == 0:
                    check_see(0,cord,board)
                    check_see(1,cord,board)
                    check_see(3,cord,board)
                elif d == 1:
                    check_see(0,cord,board)
                    check_see(1,cord,board)
                    check_see(2,cord,board)
                elif d == 2:
                    check_see(1,cord,board)
                    check_see(2,cord,board)
                    check_see(3,cord,board)
                else:
                    check_see(0,cord,board)
                    check_see(2,cord,board)
                    check_see(3,cord,board)
            else:
                check_see(0,cord,board)
                check_see(1,cord,board)
                check_see(2,cord,board)
                check_see(3,cord,board)                

        mn = min(mn,check_black(board))

    return mn


print(solution(board_og))

"""
5 5
5 1 6 1 4
6 0 1 6 3
2 5 0 0 0
0 6 0 0 0
6 0 6 6 6
"""
