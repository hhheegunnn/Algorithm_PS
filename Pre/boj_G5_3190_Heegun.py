"""https://www.acmicpc.net/problem/3190"""


""" 뱀 """

# 5:40 ~ 7:05 

# git add boj_implementation/G/G5/3190/boj_G5_3190_Heegun.py
# git commit -m "[김희건] boj 뱀"



from collections import deque

def check_in(y,x):
    if 0<= y < N and 0<= x < N:
        return True
    else:
        return False

direction = [(-1,0), (0,1), (1,0), (0,-1)]



def solution(board,snake):
    

    cnt = 0

    r = 0
    c = 0

    board[r][c] = 2
    di = 1


    while True:
        
        cnt += 1
        
        
        if check_in(r+direction[di][0],c+direction[di][1]):
            r = r+direction[di][0]
            c = c+direction[di][1]

            # 사과 있을 때 -> 뱀 머리 추가하고 머리에 2
            if board[r][c] == 1:
                snake.append((r,c))
                board[r][c] = 2

            # 사과가 없을경우 -> 뱀 머리 추가하고 머리에 2     뱀 꼬리 자르고 꼬리 위치에 0
            elif board[r][c] == 0:
                snake.append((r,c))
                tr,tc = snake.popleft()
            
                board[r][c] = 2
                board[tr][tc] = 0
            
            # 뱀 몸이 있을 경우
            elif board[r][c] == 2: 
                return cnt
        
        # 벽
        else: 
            return cnt
        


    # 방향 전환


        if Change_dir:
            command = Change_dir[0]
            if command[0] == cnt:

                Change_dir.pop(0)

                if command[1] == "L":
                    di = (di+3)%4
                else:
                    di = (di+1)%4




N = int(input())
K = int(input())
Board = [[0 for _ in range(N)] for _ in range(N)]
for _ in range(K):
    r,c = map(int,input().split())
    Board[r-1][c-1] = 1

L = int(input())
Change_dir = []
for _ in range(L):
    X, C = map(str,input().split())
    Change_dir.append((int(X),C))

Snake = deque([(0,0)])

print(solution(Board,Snake))


