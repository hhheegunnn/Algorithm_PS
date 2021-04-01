"""https://www.acmicpc.net/problem/14501"""


"""퇴사 """


##### INPUT ####


N = int(input()) ##상담가능 날짜

#board = list(tuple(map(int,input().split())) for _ in range(N))

board = []

for i in range(N):
    t,p = map(int,input().split())

    if i + t > N:
        board.append((0,0))
    else:
        board.append((t,p))

##################

#print(board)


def dp():

    dp = [0 for _ in range(N+1)]

    for i in range(N):

        if board[i][0] == 0:
            continue

        else:
            if i != 0:
                dp[i] = max(dp[i], dp[i-1])
            addIndex = board[i][0]
            dp[i+addIndex] = max(dp[i+addIndex] , board[i][1]+ dp[i])

    return max(dp)


print(dp())
        


