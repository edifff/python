def z_func(s):
    n = len(s)
    z = [0] * n
    l = 0
    r = 0
    for i in range(1, len(s)):
        z[i] = max(0, min(r - i, z[i - l]))
        # z[i] = min(z[i - l], l + z[l] - i)
        while i + z[i] < n and s[z[i]] == s[i + z[i]]:
            z[i] += 1
        # if i + z[i] > l + z[l]:
        #     l = i
        if i + z[i] > r:
            l = i
            r = i + z[i]

    return z


# print(z_func('abacaba'))

s = input()
n = int(input())

for _ in range(n):
    t = input()
    ll = len(t)

    zz = z_func(t + "#" + s)[ll+1:]

    res = []
    count = 0
    # print(zz)
    for i, item in enumerate(zz):
        if item == ll:
            res.append(i)
            count += 1

    print(count, *res)

"""
abcdaabcd
4
a
bc
e
abcdaabcd

"""