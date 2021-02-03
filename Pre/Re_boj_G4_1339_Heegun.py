"""https://www.acmicpc.net/problem/1339"""



"""단어 수학""" 


N = int(input())

w_list = []

num_list = [0,1,2,3,4,5,6,7,8,9]

w_list = [list(map(lambda x : ord(x)-65 , input())) for _ in range(N)]

alpha = [0]*26

for i in range(N):
    j = 0
    for w in w_list[i][::-1]:
        alpha[w] += (10 ** j)
        j += 1

alpha.sort(reverse=True)
print(alpha)

result = 0
for i in range(26):
    if alpha[i] == 0:
        break
    result += (num_list.pop() * alpha[i])

print(result)
