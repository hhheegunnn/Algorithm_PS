"""https://programmers.co.kr/learn/courses/30/lessons/42883"""

""" 큰 수 만들기 """



# no greedy  조합 완탐 시간초과

from itertools import combinations

def combination_solution(number,k):


    num = list(number)



    num_list = combinations(num,len(number)-k)
    t = list(max(num_list))
    result = ''.join(t)

    return result


def solution(number,k):

    stack = []

    for num in number:

        while stack and num > stack[-1] and k >0:
            stack.pop()
            k -= 1

        stack.append(num)

    
    if k != 0:
        stack = stack[:-k]

    return ''.join(stack)
        

print(solution('1924',2))
print(solution('1231234',3))
print(solution('4177252841',4))
print(solution('11111',4))
print(solution('54321',2))










