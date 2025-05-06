import sys
import queue

card_queue = queue.Queue()
N = int(sys.stdin.readline())

for i in range(1, N+1):
    card_queue.put(i)

while card_queue.qsize() != 1:
    card_queue.get()
    card_queue.put(card_queue.get())
print(card_queue.get())
