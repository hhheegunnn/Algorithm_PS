"""https://www.acmicpc.net/problem/2751"""



"""수 정렬하기2"""

# git add week_06/boj_S5_2751_Heegun.py
# git commit -m "[김희건] boj 수 정렬하기2 [퀵 소트 시간초과나는 이유, 계수 정렬 확인]"

import sys
sys.setrecursionlimit(1000000000)
input = sys.stdin.readline

N = int(input())
result = [int(input()) for _ in range(N)]

#print(result)



def sort_lib(): # 파이썬 정렬 라이브러리 시간초과

    result.sort()


def selection_sort(): # 선택 정렬 시간 초과
    
    for i in range(N):
        min_index = i
        for j in range(i,N):
            if result[min_index] > result[j]:
                min_index = j
            else:
                continue
        result[i], result[min_index] = result[min_index], result[i]


def insertion_sort():

    for i in range(1,N):
        for j in range(i,0,-1):
            if result[j] < result[j-1]:
                result[j], result[j-1] = result[j-1], result[j]
            else:
                break


def quick_sort(result, start, end):

    if len(result) <= 1:
        return result

    pivot = start
    left = start + 1
    right = end

    while left <= right:

        while left <= end and result[left] <= result[pivot]:
            left += 1
        
        while right > start and result[right] >= result[pivot]:
            right -= 1

        if left > right:
            result[right], result[pivot] = result[pivot], result[right]
        else:
            result[left], result[right] = result[right], result[left]


        quick_sort(result, start,right-1)
        quick_sort(result, right+1, end)


def counting_sort():

    arr = [False]*2000001

    for i in result:
        arr[i+1000000] = True
    
    for i in range(len(arr)):
        if arr[i] == True:
            print(i-1000000)




# 파이썬 정렬 라이브러리 시간초과 sys.stdin사용 통과
sort_lib() 

# 선택 정렬 시간 초과
# selection_sort() 

# 삽입 정렬 시간 초과
#insertion_sort()

# 퀵 정렬 시간 초과 왜 나는지 잘 모르겠다(NlogN인데)
#quick_sort(result,0,N-1)

for i in result:
    print(i)

# 계수 정렬 sys.stdin사용 통과
# counting_sort()












