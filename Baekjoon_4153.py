while True:
    a, b, c = map(int, input().split())
    if a == 0 and b == 0 and c == 0:
        break

    sort_num = sorted([a, b, c])
    if sort_num[0]**2 + sort_num[1]**2 == sort_num[2]**2:
        print('right')
    else:
        print('wrong')
