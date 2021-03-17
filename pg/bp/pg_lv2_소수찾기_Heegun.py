"""https://programmers.co.kr/learn/courses/30/lessons/42839"""


"""소수 찾기"""

"""
from math import sqrt
from itertools import permutations
def find_prime(d):
    max_num = 0
    prime = []
    for i in range(d):
        max_num += 9*(10**(i))
    check = [True]*max_num

    m = int(sqrt(max_num))

    for i in range(2,m+1):
        if check[i] == True:
            for j in range(i+i,max_num,i):
                check[j] = False
    
    for i in range(2,max_num):
        if check[i] == True:
            prime.append(i)

    return prime
    
def solution(numbers):
    prime_num = find_prime(len(numbers))

    numbers = list(numbers)

    full_list = []

    for i in range(1,len(numbers)+1):

        tmp = list(permutations(numbers,i))

        for t in tmp:
            n = int(''.join(t))

            if n not in full_list:
                full_list.append(n)
        
    #print(full_list)
    cnt = 0

    for i in full_list:
        if i in prime_num:
            cnt += 1

    return cnt
"""

from math import sqrt
from itertools import permutations

def isPrime(x):
    if x<2:
        return False
    else:
        for i in range(2,int(sqrt(x))+1):
            if x%i == 0:
                return False
    
    return True

def solution(numbers):

    cnt = 0
    test=[]

    for i in range(len(numbers)):
        case = list(set(map(''.join,permutations(numbers,i+1))))

        for n in case:
            test.append(int(n))

    test = list(set(test))
    for n in test:
        if isPrime(n):
            cnt += 1

    return cnt


print(solution("17"))

        

     

        