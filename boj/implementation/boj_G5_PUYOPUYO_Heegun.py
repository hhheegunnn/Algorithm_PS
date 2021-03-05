"""https://www.acmicpc.net/problem/11559"""


"""Puyo Puyo"""



from collections import deque


R = 12
C = 6


board = [list(input()) for _ in range(12)]

def down_puyo():
    
    for x in range(C):
        for y in range(R-1,-1,-1):
            if board[y][x] != '.':
                #한줄씩 내린다
                i = y   
                j = x
                while True:
                    if i >= R-1:
                        break
                    else:
                        if board[i+1][j] == '.':
                            board[i+1][j] = board[i][j]
                            board[i][j] = '.'
                            i += 1
                        else:
                            break
            else:
                continue

    

def erase_puyo(cord):
    for i,j in cord:
        board[i][j] = '.'


def bfs(y,x,color):

    visited = [[False for _ in range(C)] for _ in range(R)]

    cnt = 1
    erase_cord = []

    q = deque([(y,x)])
    erase_cord = [(y,x)]

    visited[y][x] = True

    while q:

        node_y, node_x = q.popleft()

        for d in [(-1,0),(0,1),(1,0),(0,-1)]:
            next_y = node_y + d[0]
            next_x = node_x + d[1]

            if 0<=next_x<C and 0<=next_y<R:
                if not visited[next_y][next_x] and board[next_y][next_x] == color:
                    q.append((next_y,next_x))
                    visited[next_y][next_x] = True
                    cnt += 1
                    erase_cord.append((next_y,next_x))

    if cnt >= 4:
        erase_colors.append(color)
        erase_puyo(erase_cord)

    else:
        return

result = 0


while True:

    erase_colors = []

    for r in range(R):
        for c in range(C):
            if board[r][c] != '.':
                bfs(r,c,board[r][c])

    if not erase_colors:
        break

    down_puyo()
    result += 1


print(result)
