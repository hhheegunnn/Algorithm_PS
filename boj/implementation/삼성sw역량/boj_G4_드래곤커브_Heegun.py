"""https://www.acmicpc.net/problem/15685"""


"""드래곤 커브"""


N = int(input())

curves = []

for _ in range(N):

    x, y, d, g = map(int,input().split())

    curves.append((x,y,d,g))

board = [[0 for _ in range(101)] for _ in range(101)]

def draw(x,y,d,g):

    delta =[(0,1),(-1,0),(0,-1),(1,0)]

    d_list = [d]

    for _ in range(g):

        for i in range(len(d_list)-1,-1,-1):
            next_d = (d_list[i]+1)%4
            d_list.append(next_d)


    for dt in d_list:

        board[y][x] = 1

        y += delta[dt][0]
        x += delta[dt][1]

        if 0 <= y < 101 and 0<= x < 101:

            if board[y][x] == 0:
                board[y][x] = 1

def find_square():

    result = 0

    for r in range(101):
        for c in range(101):

            cnt = 0

            if board[r][c] == 1:

                for dr,dc in [(1,0),(1,1),(0,1)]:
                    nr,nc = r+dr, c+dc

                    if 0<= nr < 101 and 0<=nc < 101 and board[nr][nc] == 1:

                        cnt += 1
                    else:
                        break
            if cnt == 3:
                result += 1

    return result

def solution():

    for curve in curves:

        draw(curve[0], curve[1], curve[2], curve[3])

    r = find_square()

    return r

print(solution())