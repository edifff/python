import sys

maxn = 10005
k = 31
mod = 10 ** 9 + 7

def hash_func(s):
    p = [1] * (len(s) + 1)
    h = [0] * (len(s) + 1)
    for i in range(len(s)):
        h[i + 1] = (h[i] * k + ord(s[i])) % mod
        p[i + 1] = (p[i] * k) % mod
    return h, p


def get_hash_sub(h, p, l, r):
    return (h[r] - h[l - 1] * p[r - l + 1] % mod + mod) % mod
s = input()
h, p = hash_func(s)
n = int(input())
for _ in range(n):
    l1, r1, l2, r2 = map(int, sys.stdin.readline().split())
    if get_hash_sub(h,p,l1,r1) == get_hash_sub(h,p, l2, r2):
        sys.stdout.write("Yes\n")
    else:
        sys.stdout.write("No\n")