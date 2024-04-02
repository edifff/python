from heapq import heappop, heappush
import sys


def heap_sort(ls):
    heap = []
    for num in ls:
        heappush(heap, num)

    res = []
    while heap:
        res.append(heappop(heap))

    return res


if __name__ == "__main__":
    n = int(input())
    ls = list(map(int, input().split()))

    res = heap_sort(ls)

    for num in res:
        sys.stdout.write(str(num) + " ")

