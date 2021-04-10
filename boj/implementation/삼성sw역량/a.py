from collections import defaultdict


a = defaultdict()

for i in [1,2,3,2,4,1,5]:

    if i in a.keys():
        a[i] += 9
    else:
        a[i] = 9

print(a)