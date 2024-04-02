a = input()
b = input()

n = len(b)

b += b

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


#
def get_hash_sub(h, p, l, r):
    return (h[r] - h[l - 1] * p[r - l + 1] % mod + mod) % mod


ha, pa = hash_func(a)
hb, pb = hash_func(b)
# print(ha, hb)
hashes_b = set()
for i in range(n):
    # print(b[i+1:i + n+1])
    hashes_b.add(get_hash_sub(hb, pb, i+1, i + n))

# print(hashes_b)

res = 0
for i in range(len(a) - n+1):
    # print(i, i + n)
    hash_a = get_hash_sub(ha, pa, i+1, i + n)
    # print(hash_a, a[i:i+n])
    if hash_a in hashes_b:
        res += 1

print(res)

"""
abcabc
abc

abcabc
acb

aaaaaaa
aa

aAaa8aaAa
aAa

"""