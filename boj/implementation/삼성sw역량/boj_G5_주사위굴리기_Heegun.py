"""https://www.acmicpc.net/problem/14499"""


"""주사위굴리기"""


#############

N , M, sr, sc, k = map(int,input().split())

board = [list(map(int,input().split())) for _ in range(N)]

command = list(map(int,input().split()))


#############

def move_dice(dice,di):

    tmp = [0 for _ in range(7)]
    if di == 1:
        tmp[1],tmp[2],tmp[3],tmp[4],tmp[5],tmp[6] = dice[4],dice[2],dice[1],dice[6],dice[5],dice[3]
    elif di == 2:
        tmp[1],tmp[2],tmp[3],tmp[4],tmp[5],tmp[6] = dice[3],dice[2],dice[6],dice[1],dice[5],dice[4]
    elif di == 3:
        tmp[1],tmp[2],tmp[3],tmp[4],tmp[5],tmp[6] = dice[5],dice[1],dice[3],dice[4],dice[6],dice[2]
    else:
        tmp[1],tmp[2],tmp[3],tmp[4],tmp[5],tmp[6] = dice[2],dice[6],dice[3],dice[4],dice[1],dice[5]
        
    return tmp


def solution(sr,sc):

    d = [(0,0),(0,1),(0,-1),(-1,0),(1,0)]

    dice = [0 for _ in range(7)]

    for di in command:

        if 0<= sr + d[di][0] < N and 0<= sc + d[di][1] < M:
            sr += d[di][0]
            sc += d[di][1]

            dice = move_dice(dice,di)

            if board[sr][sc] == 0:
                board[sr][sc] = dice[6]
            else:
                dice[6] = board[sr][sc]
                board[sr][sc] = 0

            print(dice[1])
        else:
            continue
    

solution(sr,sc)

