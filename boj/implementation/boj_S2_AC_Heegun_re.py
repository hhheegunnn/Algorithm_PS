"""https://www.acmicpc.net/problem/5430"""


"""AC"""

from collections import deque

T = int(input())

for _ in range(T):

    p = list(input())

    n = int(input())

    numbers = deque(input()[1:-1].split(','))


    if n == 0:
        numbers = []

    flag =True
    reverse_flag = -1
    for i in p:
        if i == 'R':
            reverse_flag *= -1
        else:
            if numbers:
                if reverse_flag == 1:
                    numbers.pop()
                else:
                    numbers.popleft()
            else:
                flag = False
                break
    

    if flag:
        if reverse_flag == 1:
            print('[' + ','.join(reversed(numbers)) + ']')
        else:
            print('[' + ','.join(numbers) + ']')
    else:
        print('error')