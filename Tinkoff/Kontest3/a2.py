def find_diameter(tree):
    def dfs(node, depth):
        nonlocal max_depth, max_node
        visited.add(node)
        if depth > max_depth:
            max_depth = depth
            max_node = node
        for child in tree.get(node, []):
            if child not in visited:
                dfs(child, depth + 1)

    max_depth = -1
    max_node = None
    visited = set()

    # Начинаем с произвольной вершины (в данном случае с корня дерева)
    root = next(iter(tree))
    dfs(root, 0)

    # Повторяем DFS из найденной вершины, чтобы найти вторую самую удаленную вершину
    max_depth = -1
    visited = set()
    dfs(max_node, 0)

    return