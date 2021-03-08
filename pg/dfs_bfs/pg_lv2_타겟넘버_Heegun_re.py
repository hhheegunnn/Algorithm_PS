"""https://programmers.co.kr/learn/courses/30/lessons/43165"""


"""타겟 넘버"""




def solution(numbers, target):

    if not numbers and target == 0 :
        return 1 
    
    elif not numbers:
        return 0
    
    else:
        return solution(numbers[1:],target-numbers[0]) + solution(numbers[1:],target+numbers[0])


print(solution([1, 1, 1, 1, 1],3))


"""
answer = 0

def dfs(idx,numbers, target, value):
    global answer

    N = len(numbers)

    if (idx == N and target == value):
        answer += 1
        return
    if idx == N:
        return

    dfs(idx+1, numbers,target,value+numbers[idx])
    dfs(idx+1, numbers,target,value-numbers[idx])

def solution_(numbers, target):
    global answer
    dfs(0,numbers,target,0)
    return answer
"""

"""
def dfs(nums, i, n, t):
    ret = 0
    if i==len(nums):
        if n==t: return 1
        else: return 0
    ret += dfs(nums, i+1, n+nums[i], t)
    ret += dfs(nums, i+1, n-nums[i], t)
    return ret

def solution(numbers, target):
    answer = dfs(numbers, 0, 0, target)
    return answer
"""