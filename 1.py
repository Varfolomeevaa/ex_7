ptr = input().split()
words = {}

for i in range(len(ptr)):
    if ptr[i] in words:
        words[ptr[i]] += 1
    else:
        words[ptr[i]] = 1


counts = list(words.values())
counts.sort(reverse=True)

for i in range(len(counts)):
    for j in words:
        if counts[i] == words[j]:
            print(j)
