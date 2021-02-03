"""https://www.acmicpc.net/problem/2670"""



"""연속부분최대곱"""

# git add week_08/Re_boj_S4_2670_Heegun.py
# git commit -m "[김희건] boj 연속부분최대곱 [파이썬 실수 계산 decimal]"

from decimal import Decimal
import sys

input = sys.stdin.readline

n = int(input())


num_list = list(Decimal(input()) for _ in range(n))

max_p = num_list[0]
tmp = [0 for _ in range(10)]
tmp[0] = num_list[0]

for i in range(1,n):
    
    # i-1번째 최대 값과 i번째 값을 곱한 값이 i 번째 값보다 크다면 i번째 최대값을 곱한수로 아니면 i번째 수를 최대값으로
    if tmp[i-1]*num_list[i] > num_list[i]:
        tmp[i] = tmp[i-1]*num_list[i]
    else:
        tmp[i] = num_list[i]
    
    if (max_p < tmp[i]):
        max_p = tmp[i]
    #print(tmp)



    

print(round(max_p,3))
    






