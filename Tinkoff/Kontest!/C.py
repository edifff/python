import sys
def q(x):
    print(x)
    sys.stdout.flush()
    return input()

inp=int(input())

l=0
r=inp+1
while r-l>1:
    m=(l+r)//2
    s=q(m)
    if s=='<':
        r=m
    elif s=='>=':
        l=m

print('! '+str(l))