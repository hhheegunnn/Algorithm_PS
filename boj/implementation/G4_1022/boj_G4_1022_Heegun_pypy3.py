"""https://www.acmicpc.net/problem/1022"""



""" 소용돌이 예쁘게 출력하기  메모리 개선 """



# pypy3 통과  python3 시간초과


def cyclone(r1,c1,r2,c2,total_num):

    r = 0
    c = 0

    num = 1
    cnt = 1
    dcnt = 0

    dr = [0,-1,0,1]
    dc = [1,0,-1,0]

    while total_num > 0:


        
        for _ in range(2):

            for _ in range(cnt):

                if r1 <= r <= r2 and c1<=c<=c2:
                    total_num -= 1
                    board[r-r1][c-c1] = num
                    max_num = num
                
                num += 1

                r += dr[dcnt]
                c += dc[dcnt]

            dcnt = (dcnt+1)%4           

        cnt += 1


    return board,len(str(max_num))




r1,c1,r2,c2 = map(int,input().split())

total_num = (r2-r1+1) * (c2-c1+1)

board = [[0 for _ in range(c2-c1+1)] for _ in range(r2-r1+1)]


result,digit = cyclone(r1,c1,r2,c2,total_num)

for r in result:
    for rr in r:
        print(str(rr).rjust(digit),end = ' ')
    print()










