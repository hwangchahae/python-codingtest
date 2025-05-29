import sys
from collections import deque
input = sys.stdin.readline
N, K = map(int, input().split())

dq = deque(range(1, N+1))
result = []

while(len(dq)>0):
    for _ in range(K-1):
        dq.append(dq.popleft())
    result.append(dq.popleft())

print(f"<{', '.join(map(str, result))}>")
