N = int(input())
sizes = list(map(int, input().split()))
T, P = map(int, input().split())

total_sum = 0
for size in sizes:
    t = size // T + 1
    if size % T == 0 :
        t -= 1
    total_sum += t 
print(total_sum)
print(N//P, N % P)
