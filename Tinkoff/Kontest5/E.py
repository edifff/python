def find_approximate_substrings(t, p):
    substrings = []
    for i in range(len(t) - len(p) + 1):
        mismatch_count = 0
        for j in range(len(p)):
            if t[i+j] != p[j]:
                mismatch_count += 1
                if mismatch_count > 1:
                    break
        if mismatch_count <= 1:
            substrings.append(i+1)
            # substrings.append(t[i:i+len(p)])
    return substrings

p = input()
t = input()
result = find_approximate_substrings(t, p)
print(len(result))
print(*result)