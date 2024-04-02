from math import sqrt
def fR(c):
    x = 1
    while f(x) < c:
        x = x * 2
    return x
def fL(c):
    x = -1
    while f(x) > c:
        x = x * 2
    return x
def f(x):
    return x ** 2 + sqrt(x + 1)

t = 1e-10
c = float(input())

l = fL(c)
fs = fR(c)
while (fs - l) > t:
    mid = (l + fs) / 2
    if f(mid) < c:
        l = mid
    else:
        fs = mid

print((l + fs) / 2)