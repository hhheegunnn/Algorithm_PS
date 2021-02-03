"""https://programmers.co.kr/learn/courses/30/lessons/42747"""


"""H-inex"""

# git add week_07/pg_lv2_42747_Heegun.py
# git commit -m "[김희건] pg H-INDEX"

"""
def solution(citations):
    citations.sort()

    result =[]
    n = len(citations)

    for h in range(n+1):
        cnt = 0
        for j in citations:
            if h <= j:
                cnt += 1
        
        if cnt >= h :
            result.append(h)
        
    
    #print(result)
    return max(result)

"""

def solution(citations):
    citations = sorted(citations)
    l = len(citations)
    for i in range(l):
        if citations[i] >= l-i:
            return l-i
    return 0

print(solution([20,21,22,23] ))
print(solution([4,4,4] ))




