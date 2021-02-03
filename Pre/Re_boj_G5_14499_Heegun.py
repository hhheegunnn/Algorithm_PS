"""https://www.acmicpc.net/problem/14499"""


"""주사위 굴리기"""

# git add boj_implementation/G/G5/14499/Re_boj_G5_14499_Heegun.py
# git commit -m "[김희건] boj 주사위 굴리기 [매우 아깝, 주사위 전개도 고정에 위의 인덱스만 조정]"

direction = [(0,0), (0,1), (0,-1), (-1,0), (1,0)]

def check_in(r,c):
    if 0<= r < N and 0<= c < M:
        return True
    else:
        return False

def dice_roll(com,dice):

    if com == 1:
        dice[1], dice[3], dice[4], dice[6] = dice[4], dice[1], dice[6], dice[3]
    elif com == 2:
        dice[1], dice[3], dice[4], dice[6] = dice[3], dice[6], dice[1], dice[4]
    elif com == 3:
        dice[1], dice[2], dice[5], dice[6] = dice[5], dice[1], dice[6], dice[2]
    else:
        dice[1], dice[2], dice[5], dice[6] = dice[2], dice[6], dice[1], dice[5]


def solution(board, command, r, c, dice):


    for i in command:

        if check_in(r + direction[i][0], c + direction[i][1]):
            r += direction[i][0]
            c += direction[i][1]

            dice_roll(i,dice)
 
            if board[r][c] == 0:
                board[r][c] = dice[6]
                print(dice[1])
            else:
                dice[6] = board[r][c]
                board[r][c] = 0
                print(dice[1])

        else:
            continue



N, M , x, y , k = map(int,input().split())
# N x r     # M y c
Board = [list(map(int,input().split())) for _ in range(N)]
Command = list(map(int,input().split()))
Dice = [0 ,0,0,0,0,0,0]

solution(Board, Command, x, y, Dice)