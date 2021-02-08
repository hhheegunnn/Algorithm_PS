"""https://www.acmicpc.net/problem/1022"""


""" 소용돌이 예쁘게 출력하기 """


# 메모리 초과



def cyclone():

    max_num = len(board)**2
    r, c = len(board)//2,len(board)//2
    
    board[r][c] = 1

    d = [(0,1), (-1,0), (0,-1), (1,0)]
    
    num = 2
    dcnt = 0
    cnt = 1

    while True:
        
        for _ in range(2):

            for _ in range(cnt):

                r = r + d[dcnt][0]
                c = c + d[dcnt][1]

                board[r][c] = num

                num += 1

                if num > max_num:
                    return

            dcnt =  (dcnt+1)%4

        cnt += 1

def solution(r1,c1,r2,c2):
    
    sr = r1 + test
    sc = c1 + test
    er = r2 + test
    ec = c2 + test

    result = []

    max_n = 0



    for i in range(sr,er+1):
        tmp = board[i][sc:ec+1]
        max_n=max(max(tmp),max_n)
        result.append(tmp)

    
    digit = len(str(max_n))

    for r in result:
        for j in r:
            jj = str(j).rjust(digit,' ')
            print(jj,end=' ')
        print()

    return






r1,c1,r2,c2 = map(int,input().split())


kr = 0
kc = 0
if abs(r1) >= abs(r2):
    kr = abs(r1)
else:
    kr = abs(r2)

if abs(c1) >= abs(c2):
    kc = abs(c1)
else:
    kc = abs(c2)


test = max(kr,kc)
print(test)

board = [[0 for _ in range(test*2+1)] for _ in range(test*2+1)]


cyclone()
solution(r1,c1,r2,c2)

