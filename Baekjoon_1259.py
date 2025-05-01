while(True):
    word = input()
    if word == '0':
        break
    for i in range(1, len(word)//2 + 1):
        if word[i] != word[-i]:
            print('no')
            break
    else :
        print('yes')
