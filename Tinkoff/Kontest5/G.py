import random

k = 31
mod = 10 ** 9 + 7

n = int(input())
ls1 = list(map(int, input().split()))

m = int(input())
ls2 = list(map(int, input().split()))

dc2 = {}

for i, item in enumerate(sorted(set(ls1) | set(ls2))):
    dc2[item] = i

dcHash = {item: random.randint(1, 10 ** 9) * k for item in dc2.values()}

ls1 = list(map(lambda x: dc2[x], ls1))
ls2 = list(map(lambda x: dc2[x], ls2))

if len(set(ls1) & set(ls2)) == 0:
    print(0)
    exit(0)

sum1 = [0] * (len(ls1) + 1)
sum2 = [0] * (len(ls2) + 1)

for i, item in enumerate(ls1, start=1):
    sum1[i] = sum1[i - 1] + dcHash[item]

for i, item in enumerate(ls2, start=1):
    sum2[i] = sum2[i - 1] + dcHash[item]

l = min(len(ls1), len(ls2))

for i in range(l, 0, -1):
    for k in range(len(ls1) - i + 1):
        sub1 = sum1[k + i] - sum1[k]
        for j in range(len(ls2) - i + 1):
            sub2 = sum2[j + i] - sum2[j]
            if sub1 == sub2:
                print(i)
                exit(0)

else:
    print(0)
