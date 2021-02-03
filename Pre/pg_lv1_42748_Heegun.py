"""https://programmers.co.kr/learn/courses/30/lessons/42748"""


"""K번째수"""

# git add week_07/pg_lv1_42748_Heegun.py
# git commit -m "[김희건] pg k번째수"

def solution(array, commands):

    result = []

    for c in commands:
        tmp = sorted(array[c[0]-1:c[1]])
        result.append(tmp[c[2]-1])

    return result


print(solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]	))
