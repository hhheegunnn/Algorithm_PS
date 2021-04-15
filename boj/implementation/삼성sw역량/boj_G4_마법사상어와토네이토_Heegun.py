"""https://www.acmicpc.net/problem/20057"""


""" 마법사 상어와 토네이도 """


N = int(input())

board = [list(map(int,input().split())) for _ in range(N)]



def spread(r,c,d):

    total_sand = board[r][c]
    sand = 0
    tmp_result = 0
    alph_sand=0

    percent = [2,2,7,7,1,1,10,10,5]
    
    d0r = [-2,2,-1,1,-1,1,-1,1,0,0]
    d0c = [0,0,0,0,1,1,-1,-1,-2,-1]

    d1r = [0,0,0,0,-1,-1,1,1,2,1]
    d1c = [-2,2,-1,1,-1,1,-1,1,0,0]

    d2r = [-2,2,-1,1,-1,1,-1,1,0,0]
    d2c = [0,0,0,0,-1,-1,1,1,2,1]

    d3r = [0,0,0,0,1,1,-1,-1,-2,-1]
    d3c = [-2,2,-1,1,-1,1,-1,1,0,0]

    if d == 0:
        dr = d0r
        dc = d0c
    elif d == 1:
        dr = d1r
        dc = d1c
    elif d == 2:
        dr = d2r
        dc = d2c
    else:
        dr = d3r
        dc = d3c

    for i in range(10):

        nr,nc = r + dr[i] , c + dc[i]

        if i == 9:
            alph_sand = total_sand - sand
            if 0<=nr<N and 0<=nc<N:
 
                board[nr][nc] += alph_sand
            else:

                tmp_result += alph_sand

        else:
            if 0<=nr<N and 0<=nc<N:
                in_sand = (total_sand*percent[i])//100
                sand += in_sand
                board[nr][nc] += in_sand

            else:
                out_sand = (total_sand*percent[i])//100
                sand += out_sand
                tmp_result += out_sand

    board[r][c] = 0

    return tmp_result



def solution():

    delta = [(0,-1),(1,0),(0,1),(-1,0)]

    result = 0

    r,c = N//2,N//2
    d = 0
    for i in range(1,N):  # 전진 횟수

        for _ in range(2): # 전진 횟수당 이동 횟수

            for _ in range(i): # 실제 전진
                r += delta[d][0]
                c += delta[d][1]

                t_r = spread(r,c,d)

                result += t_r

            d = (d+1)%4

    d = 0
    for i in range(N-2,-1,-1):
        t_r = spread(0,i,d)
        result += t_r

    return result

print(solution())

