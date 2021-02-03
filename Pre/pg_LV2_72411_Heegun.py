"""https://programmers.co.kr/learn/courses/30/lessons/72411"""

"""  메뉴 리뉴얼 """

# git add week_13/pg_LV2_72411_Heegun.py
# git commit -m "[김희건] pg 메뉴 리뉴얼"


# 복잡한데 시간은 더 빠름
"""
from collections import defaultdict
from itertools import combinations

def solution(orders,course):

    answer = []

    for c in course:

        tmp = []
        hmap = defaultdict(lambda : 0)

        for i in range(len(orders)):
            orders[i] = ''.join(sorted(orders[i]))
            

        for o in orders:
            tmp = list(combinations(o,c))

            for i in tmp:
                i = str(i)

                hmap[i] += 1

        if not hmap:
            continue

        max_n = max(hmap.values())
        max_nn = []
        
        for key, value in hmap.items():
            if value == max_n:
                if value >= 2:
                    max_nn.append(key)
        

        for i in max_nn:
            k = ''
            for j in i:
                if 'A' <= j <= "Z":
                    k += j
            answer.append(k)

    answer.sort()
        
    return answer
"""

# 간결한데 시간은 더걸림...

from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []

    for c in course:
        tmp = []

        for order in orders:
            combi = combinations(sorted(order),c)
            tmp += combi
        
        counter = Counter(tmp)
        
        if len(counter) != 0 and max(counter.values()) != 1:
            for f in counter:
                if counter[f] == max(counter.values()):
                    answer.append(''.join(f))


    return sorted(answer)



print(solution(["XYZ", "XWY", "WXA"],[2,3,4]))