N = int(input())
nums = map(int, input().split())
result = []

for num in nums:
    if num != 1:
        for i in range(2, int(num**0.5)+1):
            if num%i == 0:
                    break
        else :
            result.append(num)
print(len(result))                         
