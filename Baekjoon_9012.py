T = int(input())

for _ in range(T):
    result = []
    ps = input()
    for s in ps:
        if not result and s == ')':
            print('NO')
            break
        else:
            if s == '(':
                result.append(s)
            else:
                result.pop()
    if len(result) == 0:
        print('YES')
    else:
        print('NO')
