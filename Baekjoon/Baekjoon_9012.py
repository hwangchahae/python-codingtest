T = int(input())

for _ in range(T):
    result = []
    answer = ''
    ps = input()
    for s in ps:
        if not result and s == ')':
            answer = 'NO'
            break
        else:
            if s == '(':
                result.append(s)
            else:
                result.pop()

    if not result and answer == '':
        print('YES')
    else:
        print('NO')
