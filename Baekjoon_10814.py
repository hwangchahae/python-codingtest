import sys

N = int(sys.stdin.readline())
age_name=[]

for _ in range(N):
    age, name = sys.stdin.readline().split()
    age_name.append([int(age), name])

    
age_name = sorted(age_name, key = lambda x : x[0])   

for r in range(N):
    print(age_name[r][0], age_name[r][1])
