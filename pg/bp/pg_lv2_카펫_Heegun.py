"""https://programmers.co.kr/learn/courses/30/lessons/42842"""


"""카펫"""


def solution(brown,yellow):
    
    xsumy = (brown+4)//2
    result = []
    for x in range(3,xsumy//2+1):
        if (x-2)*(xsumy-x-2) == yellow:
            result.append(xsumy-x)
            result.append(x)
            break

    return result

print(solution(24,24))
            


