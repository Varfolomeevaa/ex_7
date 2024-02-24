number = int(input())
words_1 = {}
words_2 = {}

for i in range(number):
    ptr = input().split()
    words_1[ptr[0]] = ptr[1]
    words_2[ptr[1]] = ptr[0]

word = input()

if word in words_1:
    print(words_1[word])
elif word in words_2:
    print(words_2[word])
else:
    print(word)
