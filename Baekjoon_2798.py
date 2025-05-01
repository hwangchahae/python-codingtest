N, M = map(int, input().split())
cards = list(map(int, input().split()))

total = 0
max_total = 0

for i, a in enumerate(cards[:-2]):
    b_idx = i + 1
    for j, b in enumerate(cards[b_idx:-1]):
        c_idx = b_idx + j + 1
        for c in cards[c_idx:]:
            total = a+b+c
            if (total <= M) and (max_total < total):
                max_total = total
            
print(max_total)
