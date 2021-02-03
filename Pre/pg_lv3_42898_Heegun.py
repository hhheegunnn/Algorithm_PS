"""https://programmers.co.kr/learn/courses/30/lessons/42898"""


"""등굣길"""


# git add week_11/pg_lv3_42898_Heegun.py
# git commit -m "[김희건] pg 등굣길"


def solution(m, n, puddles):
    c = m
    r = n

    board = [[0 for _ in range(c)] for _ in range(r)]

    for i in puddles: ######################물 웅덩이 열 행 으로 주어짐
        board[i[1]-1][i[0]-1] = -1
    

    for y in range(r):
        for x in range(c):
            if y == 0 and x == 0:
                board[y][x] = 1
                continue
            if y == 0:
                if board[y][x] == -1:
                    continue
                else:
                    if board[y][x-1] != -1:
                        board[y][x] += board[y][x-1]
                    else:
                        continue
                
            elif x == 0:
                if board[y][x] == -1:
                    continue
                else:
                    if board[y-1][x] != -1:
                        board[y][x] += board[y-1][x]
                    else:
                        continue
            
            else:
                if board[y][x] == -1:
                    continue
                else:
                    if board[y-1][x] != -1 and board[y][x-1] == -1:
                        board[y][x] += board[y-1][x]
                    elif board[y][x-1] != -1 and board[y-1][x] == -1:
                        board[y][x] += board[y][x-1]
                    elif board[y][x-1] == -1 and board[y-1][x] == -1:
                        continue
                    else:
                        board[y][x] += (board[y][x-1] + board[y-1][x])
    
    return board[r-1][c-1]%1000000007
            

                    

print(solution(4,3,[[2,2]]))

