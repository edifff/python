import sys
from collections import deque

n = int(input())

first = deque()
second = deque()

for i in range(n):
    s = sys.stdin.readline().split()
    if s[0] == "-":
        sys.stdout.write(first.popleft() + "\n")
    elif s[0] == "+":
        second.append(s[1])
    else:
        second.appendleft(s[1])

    if len(second) > len(first):
        x = second.popleft()
        first.append(x)