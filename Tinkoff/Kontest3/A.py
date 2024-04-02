n = int(input())

tree = {}
s = input().strip().split()
for i, item in enumerate(map(int, s), start=1):
    tree[item] = (tree.get(item, set()))
    tree[item].add(i)
"""
7
0 0 1 1 1 2


6
0 1 2 2 2

"""


def height(tree, v):
    if tree.get(v) is None:
        return 0
    return 1 + max(height(tree, i) for i in tree[v])


tree_ = {}

for i, item in enumerate(map(int, s), start=1):
    tree_[i] = item


def rastoynie(v):
    res = 0
    while v != 0:
        v = tree_[v]
        res += 1
        # print(tree_, v)

    return res



d = max(n - len(set(s)), 1)

print(height(tree, 0), d)

print(*(rastoynie(v) for v in range(n)))
print(tree)