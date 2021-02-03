"""https://www.acmicpc.net/problem/10815"""


"""숫자카드 """

# git add week_07/boj_S4_10815_Heegun.py
# git commit -m "[김희건] boj 숫자카드 [bisect 확인]"


from bisect import bisect_left, bisect_right


n = int(input())

card = list(map(int,input().split()))

m = int(input())

check = list(map(int,input().split()))


card.sort()


def binary_search(card,target,start,end):

    if start > end:
        return False
    
    mid = (start + end) //2

    if card[mid] == target:
        return True

    elif card[mid] > target:
        return binary_search(card, target,start, mid-1)
    
    else:
        return binary_search(card, target,mid+1, end)


result = []

for i in check:
  
    tmp = binary_search(card,i,0,n-1)
    
    if tmp:
        result.append(1)
    else:
        result.append(0)


print(*result)


bisect_result =[]
for i in check:
    if bisect_left(card,i) == bisect_right(card,i):
        bisect_result.append(0)
    else:
        bisect_result.append(1)
print(*bisect_result)