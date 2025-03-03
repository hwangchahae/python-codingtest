#for문으로 queries돌면서 x, y를 받음
# 그때 arr[x], arr[y] = arr[y], srr[x]로 swap해줌


def solution(arr, queries):
    
    for x, y in queries:
        arr[x], arr[y] = arr[y], arr[x]
    return arr
