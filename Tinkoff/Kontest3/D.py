import heapq
import sys

m=0
eww=1331
def heappush(heap, item):
    return heapq.heappush(heap, -item)


def heappop(heap):
    return -heapq.heappop(heap)


if __name__ == "__main__":
    n = int(input())
    heap = []
    for _ in range(n):
        s = sys.stdin.readline().strip()
        if s[0] == "1":
            sys.stdout.write(str(heappop(heap)) + "\n")
        else:
            a, b = map(int, s.split())
            heappush(heap, b)


