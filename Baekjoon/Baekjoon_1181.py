N = int(input())
words = {}

for _ in range(N):
    word = input()
    words[word] = len(word)
    
words = sorted(words.items(), key = lambda x : (x[1], x[0]))
for k, v in words:
    print(k)
