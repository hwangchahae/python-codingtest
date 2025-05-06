import sys
card_dict = {}
N = int(sys.stdin.readline())
for card in list(map(int, sys.stdin.readline().split())):
    if card not in card_dict:
        card_dict[card] = 1
    else :
        card_dict[card] += 1 

M = int(sys.stdin.readline())
for n in list(map(int, sys.stdin.readline().split())):
    if n in card_dict:
        print(card_dict[n], end=' ')
    else :
        print(0, end=' ')
