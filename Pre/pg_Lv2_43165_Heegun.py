"""https://programmers.co.kr/learn/courses/30/lessons/43165"""




"""타겟넘버"""

# git add week_05/pg_Lv2_43165_Heegun.py
# git commit -m "[김희건] pg 타겟넘버"


def solution(numbers, target):

    if not numbers and target == 0 :
        return 1 
    
    elif not numbers:
        return 0
    
    else:
        return solution(numbers[1:],target-numbers[0]) + solution(numbers[1:],target+numbers[0])


print(solution([1, 1, 1, 1, 1],3))

