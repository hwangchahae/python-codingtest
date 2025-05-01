while(True):
    word = input()
    if word == '0':
        break
    for i in range(0, len(word)//2):
        if word[i] != word[-(i+1)]:
            print('no')
            break
    else :
        print('yes')
     
