import sys
from collections import deque
n = int(input())
exit = 0
qu = deque()
ind = -1
cd = {}
for _ in range(n):
    s = sys.stdin.readline()
    if s[0] == "1":
        __, idx = s.split()
        ind += 1
        qu.append(idx)

        cd[idx] = ind
    elif s[0] == "2":
        qu.popleft()
        exit += 1
    elif s[0] == "3":
        idx = qu.pop()
        ind -= 1
    elif s[0] == "4":
        __, idx = s.split()
        sys.stdout.write(str(cd[idx] - exit) + "\n")

    elif s[0] == "5":
        a = qu.popleft()
        qu.appendleft(a)
        sys.stdout.write(a + "\n")
    elif s[0] == "6":
        pass