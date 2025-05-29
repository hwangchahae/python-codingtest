import sys
from collections import deque

card_deque = deque()
N = int(sys.stdin.readline())

for i in range(1, N+1):
    card_deque.append(i)

while len(card_deque) != 1:
    card_deque.popleft()
    card_deque.append(card_deque.popleft())
print(card_deque.pop())
