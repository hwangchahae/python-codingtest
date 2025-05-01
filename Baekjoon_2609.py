import math
nums = list(map(int, input().split()))

print(math.gcd(*nums))
print(math.lcm(*nums))
