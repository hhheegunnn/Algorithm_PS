"""https://programmers.co.kr/learn/courses/30/lessons/42746"""

""" 가장 큰 수"""

# git add week_07/Re_pg_lv2_42746_Heegun.py
# git commit -m "[김희건] pg 가장 큰 수"

def solution(numbers):

    # numbers의 원소가 0에서 1000이하이므로 많지 않다

    numbers = list(map(str,numbers))

    numbers.sort(key=lambda x: x*3,reverse =True)

    #print(numbers[2]*3)
    return str(int(''.join(numbers)))

print(solution([6, 10, 2]))
print(solution([3,310,301, 30, 34, 5, 9]))

