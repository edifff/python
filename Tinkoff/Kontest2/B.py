from collections import deque
def sol(array, k):
    m=[]
    d=deque()
    for i in range(len(array)):

        if len(d)>0 and d[0]<=i-k:
            d.popleft()
        while len(d)>0 and array[d[-1]]>=array[i]:
            d.pop()
        d.append(i)
        if i>=k-1:
            m.append(array[d[0]])
    return m


n,k=list(map(int, input().split()))
ls=list(map(int,input().split()))
print(*sol(ls,k))