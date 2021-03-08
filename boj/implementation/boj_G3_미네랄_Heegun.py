"""https://www.acmicpc.net/problem/2933"""


"""미네랄"""


from collections import deque


R,C = map(int,input().split())

board = [list(input()) for _ in range(R)]

N = int(input())

s_list = list(map(int,input().split()))

def print_board():
    for i in board:
        print(''.join(i))

def x_cord():

    xs = set()

    for r in range(R):
        for c in range(C):
            if board[r][c] == 'x':
                xs.add((r,c))
    return xs

def bfs(y,x):
    q = deque([(y,x)])
    x_set.remove((y,x))

    while q:
        py, px = q.popleft()

        for dy, dx in [(1,0),(0,1),(-1,0),(0,-1)]:
            ny = py + dy
            nx = px + dx

            if 0<=ny<R and 0<=nx<C:
                if board[ny][nx] == 'x' and (ny,nx) in x_set:
                    x_set.remove((ny,nx))
                    q.append((ny,nx))


def drop(x_set):
    drop_list =[[] for _ in range(C)]

    for y,x in x_set:
        drop_list[x].append(y)

    drop_cnt_list = []
    #print(drop_list)

    for i in range(len(drop_list)):
        if drop_list[i]:
            max_r = max(drop_list[i])
            k = 1
            while True:
                if max_r + k >= R or board[max_r + k][i] == 'x':
                    break
                else:
                    k += 1
            drop_cnt_list.append(k-1)
    #print(drop_cnt_list)
    drop_cnt = min(drop_cnt_list)
    for i in range(len(drop_list)):
        for j in sorted(drop_list[i],reverse=True):
            board[j+drop_cnt][i] = 'x'
            board[j][i] = '.'



for i in range(N):

    a = R - s_list[i]

    if i % 2 == 0:
        for j in range(C):
            if board[a][j] == 'x':
                board[a][j] = '.'
                break
    else:
        for j in range(C-1,-1,-1):
            if board[a][j] == 'x':
                board[a][j] = '.'
                break
    
    x_set = x_cord()
    
    
    for c in range(C):
        if (R-1,c) in x_set:
            bfs(R-1,c)
        else:
            continue
    if x_set:
        drop(x_set)

print_board()

        
