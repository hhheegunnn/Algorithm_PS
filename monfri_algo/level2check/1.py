def solution(n):

    bat = 0

    while True:

        if n == 0:
            break

        if n % 2 == 1:
            bat += 1
            n -= 1
            n = n // 2
        else:
            n = n // 2

    return bat


print(solution(5000))
