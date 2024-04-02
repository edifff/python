s = input()

res = s
for i in range(len(s)):
    s = s[-1] + s[:-1]
    res = min(s, res)

print(res)
