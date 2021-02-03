"""https://www.acmicpc.net/problem/17144"""



"""미세먼지 안녕"""


# git add boj_implementation/G/G5/17144/boj_G5_17144_Heegun.py
# git commit -m "[김희건] boj 미세먼지 안녕 [python 최적화 간당간당]"



def H():

    tmp = [[0] * C for _ in range(R)]
 

    for r in range(R):
        for c in range(C):

            if board[r][c] >= 5:
                s_air = board[r][c]//5

                
                # 방향 체크 함수사용 x -> 글로벌 불러올때 시간증가?
                for d1,d2 in (1,0), (-1,0), (0,1), (0,-1):
                    sr = r+d1
                    sc = c+d2

                    # 파이썬 최적화 인덱스 체크 함수사용 x -> 함수 사용시 시간 증가

                    if 0<= sr < R and 0<= sc < C and board[sr][sc] != -1:
                        tmp[sr][sc] += s_air
                        board[r][c] -= s_air
                        


    # 1차원 리스트로 받으면 중복되는 좌표 생성으로 인해 시간 초과 -> 똑같은 2차원 리스트 보드를 만들어 같은 좌표는 더해준다
    for i in range(R):
        for j in range(C):
            board[i][j] += tmp[i][j]

      




# ucr, ucc = 공기 청정기의 위쪽 좌표
def move_air(cr,dir):

    if dir == 1:# 공기청정기 상단
        # 1. 왼쪽 공기청정기로 들어오는 방향
        for i in range(cr - 1, 0, -1):
            board[i][0]= board[i - 1][0]
        # 2. 위쪽 
        for j in range(0, C - 1):
            board[0][j] = board[0][j + 1]
        # 3. 오른쪽 
        for i in range(0, cr):
            board[i][C - 1] = board[i + 1][C - 1]
        # 4. 공기청정기에서 나오는쪽
        for j in range(C - 1, 1, -1):
            board[cr][j] = board[cr][j - 1]
    else:
        for i in range(cr + 1, R - 1):
            board[i][0] = board[i + 1][0]
        for j in range(0, C - 1):
            board[R - 1][j] = board[R - 1][j + 1]
        for i in range(R - 1, cr, -1):
            board[i][C - 1] = board[i - 1][C - 1]
        for j in range(C - 1, 1, -1):
            board[cr][j] = board[cr][j - 1]
    board[cr][1] = 0



R,C,T = map(int,input().split())

board = [list(map(int,input().split())) for _ in range(R)]
clean = []

# H함수 내부에서 공기 청정기 값 리턴 시키면 시간초과
for i in range(R):
    if board[i][0] == -1:
        clean.append(i)
        clean.append(i+1)
        break


for _ in range(T):
    H()
    move_air(clean[0],1)
    move_air(clean[1],0)



board[clean[0]][0], board[clean[1]][0] = 0, 0
print(sum(map(sum, board)))




