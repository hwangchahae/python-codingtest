N = int(input())
nums = map(int, input().split())
result = []

for num in nums:
    if num != 1:
        for i in range(2, num+1):
            for j in range(2, int(i**0.5)+1):
                if i%j == 0:
                    break
            else :
                result.append(num)
print(len(result))            
