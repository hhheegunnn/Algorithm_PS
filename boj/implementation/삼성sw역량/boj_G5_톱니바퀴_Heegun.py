"""https://www.acmicpc.net/problem/14891"""


"""톱니바퀴"""

from collections import deque


### INPUT ###

board  = [[]]

for _ in range(4):
    board.append(deque(map(int,input())))

K = int(input())

rotate_command = [list(map(int,input().split())) for _ in range(K)]

#######
def check(wn,dd):
    rotate_list = [(wn,dd)]
    dn = wn
    ddd = dd
    un = wn
    udd = dd

    while dn:
        if dn != 1:
            if board[dn][6] == board[dn-1][2]:
                break
            else:
                rotate_list.append((dn-1,ddd*-1))
        dn -= 1
        ddd *= -1

    while un <= 4:

        if un != 4:
            if board[un][2] == board[un+1][6]:
                break
            else:
                rotate_list.append((un+1,udd*-1))
        un += 1
        udd *= -1

    return rotate_list


def rotate(r_list):

    for wn,dd in r_list:
        board[wn].rotate(dd)

def score(board):
    result = 0

    for i in range(1,5):

        if board[i][0] == 0:
            continue
        else:
            if i == 1:
                result += 1
            elif i == 2:
                result += 2
            elif i == 3:
                result += 4
            else:
                result += 8

    return result

def solution():

    for w,d in rotate_command:
        rotate_list = check(w,d)

        rotate(rotate_list)
        

    #print(board)

    answer = score(board)

    return answer



print(solution())
        


        



"""
10001111
01011101
11001110
00100010
2
3 -1
1 1
"""


