"""https://www.acmicpc.net/problem/2504"""



"""괄호의 값"""

"""boj_implementation/S/Re_boj_S2_2504_Heegun.py"""

"""[김희건] boj 괄호의 값"""

from collections import deque


input_str = input()

input_list = list(input_str)

stack = []

for i in input_list:
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
                print("0")
                exit(0)
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
                print("0")
                exit(0)
            else:
                if tmp == 0:
                    tmp = int(top)
                else:
                    tmp = tmp + int(top)
 
    else:
        stack.append(i)        

print(sum(stack))
        









