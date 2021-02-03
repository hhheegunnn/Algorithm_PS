"""https://programmers.co.kr/learn/courses/30/lessons/42883"""


"""큰 수 만들기"""

#10번 시간초과
"""
def solution(number,k):

    number = list(int(i) for i in number)
    x_length = len(number) - k

    result = []
    start = 0

    while len(result) != x_length:

        end = len(number) - (x_length - (len(result) + 1))
        tmp = [n for n in number[start:end]]

        max_tmp = max(tmp)
        result.append(max_tmp)
        start += tmp.index(max_tmp) + 1



    result = list(map(str,result))
    
    return ''.join(result)
"""

def solution(number,k):

    stack = []

    for num in number:
        while stack and stack[-1] < num and k > 0:
            k -= 1
            stack.pop()
        stack.append(num)

    if k != 0:
        stack = stack[:-k]

    return ''.join(stack)



print(solution('1924',2))
print(solution('1231234',3))
print(solution('4177252841',4))
print(solution('11111',4))
print(solution('54321',2))





        