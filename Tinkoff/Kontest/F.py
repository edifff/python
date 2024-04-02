n = int(input())
ls = list(map(int, input().split()))
cnt = 0
def sort(ls):
    if len(ls) < 2:
        return ls
    md = len(ls) // 2
    l = sort(ls[:md])
    r = sort(ls[md:])
    return merge(l, r)
def merge(ls1, ls2):
    global cnt
    i = 0
    j = 0
    r = []

    while i < len(ls1) and j < len(ls2):
        if ls1[i] <= ls2[j]:
            r.append(ls1[i])
            i += 1
        else:
            cnt += (len(ls1) - i)
            r.append(ls2[j])
            j += 1
    while i < len(ls1):
        r.append(ls1[i])
        i += 1
    while j < len(ls2):
        r.append(ls2[j])
        j += 1
    return r
res = sort(ls)
print(cnt)
print(*res)