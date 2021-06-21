from collections import deque


def AC(num_list, p):

    if len(num_list) < p.count('D'):
        return print('error')

    R_cnt = True

    for c in p:

        if c == 'R':
            R_cnt = not R_cnt

        else:
            if R_cnt:
                num_list.popleft()
            else:
                num_list.pop()

    if R_cnt:
        # print(num_list)
        return print('['+','.join(num_list)+']')
    else:
        num_list.reverse()
        return print('['+','.join(num_list)+']')


T = int(input())

for _ in range(T):

    p = input()
    n = int(input())
    num_list = input()
    num_list = num_list[1:-1]
    num_list = deque(num_list.split(','))

    if n == 0:
        num_list = []

    AC(num_list, p)
