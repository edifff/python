from collections import deque
def max_sum_times_min(n, ls):
    stack = deque()
    left = [-1] * n
    right = [n] * n
    pre_sum = [0] * n
    pre_sum[0] = ls[0]
    for i in range(1, n):
        pre_sum[i] = pre_sum[i - 1]+ls[i]

    for i in range(n):
        while stack and ls[stack[-1]] >= ls[i]:
            stack.pop()
        if stack:
            left[i] = stack[-1]
        stack.append(i)

    stack.clear()

    for i in range(n - 1, -1, -1):
        while stack and ls[stack[-1]] >= ls[i]:
            stack.pop()
        if stack:
            right[i] = stack[-1]
        stack.append(i)

    max_product = float('-inf')

    for i in range(n):
        if left[i] == -1:
            sum_sublsay = pre_sum[right[i] - 1]
        else:
            sum_sublsay = pre_sum[right[i] - 1] - pre_sum[left[i]]
        max_product = max(max_product, ls[i] * sum_sublsay)

    return max_product


if __name__ == "__main__":
    n = int(input())
    ls = list(map(int, input().split()))

    result = max_sum_times_min(n, ls)
    print(result)