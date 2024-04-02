import sys
from collections import defaultdict


def lca(tree, u, v):
    an_u = {u}
    an_v = {v}

    while u in tree or v in tree:
        if u in tree:
            u = tree[u]
            an_u.add(u)

        if v in tree:
            v = tree[v]
            an_v.add(v)

        if u in an_v:
            return u

        if v in an_u:
            return v

    return None


n = int(input())
parents = list(map(int, input().split()))
m = int(input())

tree = defaultdict(int)
# print(tree)
for i in range(1, n):
    tree[i] = parents[i - 1]


for _ in range(m):
    u, v = map(int, input().split())
    sys.stdout.write(str(lca(tree, u, v))+"\n")
