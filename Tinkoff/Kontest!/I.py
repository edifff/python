n = int(input())
p = list(map(int, input().split()))
c = 0
l = n
result =[1]
z = [0] * n
for pos in p:
    z[pos - 1] = 1
    c += 1
    if pos == l:
        while l > 0 and z[l - 1] == 1:
            l -= 1
    result.append(c - (n - l) + 1)
print(" ".join(map(str, result)))