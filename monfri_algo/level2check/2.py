def solution(n):

    result = [[0 for _ in range(i+1)] for i in range(n)]
    num = 1
    x = -1
    y = 0

    for i in range(n):
        for j in range(i, n):

            # down
            if i % 3 == 0:
                x += 1

            # right
            elif i % 3 == 1:
                y += 1

            # up
            elif i % 3 == 2:
                x -= 1
                y -= 1

            result[x][y] = num
            num += 1

    answer = sum(result, [])

    return answer


print(solution(4))
