import sys

N = int(sys.stdin.readline())

dot_list =[]

for _ in range(N):
    X, y = map(int, sys.stdin.readline().split())
    dot_list.append([X, y])
    
dot_list = sorted(dot_list, key= lambda x : (x[0], x[1]))

for _ in range(N):
    print(dot_list[0], dot_list[1])
