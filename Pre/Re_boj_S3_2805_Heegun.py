"""https://www.acmicpc.net/problem/2805"""


"""나무 자르기"""

# git add week_07/Re_boj_S3_2805_Heegun.py
# git commit -m "[김희건] boj 나무자르기 [이진탐색 반복, 재귀, 라이브러리 차이 등..]"

import sys
sys.setrecursionlimit(10**6)


n, m = map(int,input().split())

tree = list(map(int,input().split()))




def search(tree,target,start,end):

    ans = 0

    while (start<=end):
        mid = (start + end) // 2

        tree_sum = tree_cut(tree,mid)

        if tree_sum < target:
            end = mid-1

        elif tree_sum >= target:
            start = mid+1
            ans = mid
        
    
    return ans


def cut(tree,target,start,end):

    mid = (start + end) // 2

    if start == mid:
        return end if sum(map(lambda x: x-end if x > end else 0, tree)) >= m else start

    tree_sum = tree_cut(tree,mid)

    if tree_sum == target:
        return mid
    elif tree_sum < target:
        return cut(tree,target,start,mid-1)
    elif tree_sum > target:
        return cut(tree,target,mid,end)


def tree_cut(tree,cutter_hi):

    tmp = 0

    for i in tree:
        if i > cutter_hi:
            tmp += i-cutter_hi

    return tmp
        


#print(search(tree,m,0,max(tree)))
print(cut(tree,m,0,max(tree)))




        
    