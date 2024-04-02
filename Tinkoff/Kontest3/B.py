import sys

sys.setrecursionlimit(10**6)

n, r = map(int, input().split())

if n == 1:
    print(1)
    exit()

tree = [list(map(int, input().split())) for _ in range(n)]


def is_avl(tree, node, is_left, r, l):
    if is_left is not None:
        if node == -1:
            return True, 0
        if is_left and node > l:
            return False, 0
        elif not is_left and node < r:
            return False, 0

    if (tree[node][0] != -1 and tree[node][0] > node) or (tree[node][1] != -1 and tree[node][1] < node):
        return False, 0

    left_is_avl, left_height = is_avl(tree, tree[node][0], True, None,
                                      min(node, tree[node][0]))
    right_is_avl, right_height = is_avl(tree, tree[node][1], False,
                                        max(node, tree[node][1]), None)

    if not left_is_avl or not right_is_avl:
        return False, 0

    if abs(left_height - right_height) > 1:
        return False, 0

    return True, max(left_height, right_height) + 1


result, _ = is_avl(tree, r, None, 0, 0)
print(1 if result else 0)