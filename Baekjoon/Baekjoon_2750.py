import sys
import heapq

input_ = sys.stdin.readline
sort_heap = []

N = int(input_())

for _ in range(N):
    heapq.heappush(sort_heap, int(input_()))
for _ in range(N):
    print(heapq.heappop(sort_heap))
