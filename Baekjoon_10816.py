import sys
from collections import Counter

N = int(sys.stdin.readline())
cards = list(map(int, sys.stdin.readline().split()))
card_counter = Counter(cards) 

M = int(sys.stdin.readline())
targets = list(map(int, sys.stdin.readline().split()))

for n in targets:
    print(card_counter[n], end=' ')
