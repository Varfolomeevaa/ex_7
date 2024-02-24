ptr = input().split()
words = {}

for i in range(len(ptr)):
    if ptr[i] in words:
        words[ptr[i]] += 1
    else:
        words[ptr[i]] = 1

for i in sorted(words.items(), reverse=True):
    print(i[0])
