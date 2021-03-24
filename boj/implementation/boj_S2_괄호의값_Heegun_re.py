"""https://www.acmicpc.net/problem/2504"""


"""괄호의 값"""




array = input()

array = list(array)

def solution(array):
    
    stack = []

    for i in array:

        if i == ")":
            tmp = 0

            while stack:
                top = stack.pop()
                if top == "(":
                    if tmp == 0:
                        stack.append(2)
                    else:
                        stack.append(2*tmp)
                    break
                elif top == "[":
                    return 0
                else:
                    if tmp == 0:
                        tmp = int(top)
                    else:
                        tmp = tmp + int(top)


        elif i == "]":
            tmp = 0
    
            while stack:
                top = stack.pop()
                if top == "[":
                    if tmp == 0:
                        stack.append(3)
                    else:
                        stack.append(3 * tmp)
                    break
                elif top == "(":
                    return 0 
                else:
                    if tmp == 0:
                        tmp = int(top)
                    else:
                        tmp = tmp + int(top)
        else:
            stack.append(i)


    for i in stack:
        if type(i) is not int:
            return 0
    return sum(stack)

print(solution(array))

