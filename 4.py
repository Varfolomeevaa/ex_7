number = int(input())
words = {}

for i in range(number):
    ptr = input().split()
    words[ptr[0]] = ptr[1:]

word = input()

for i in words:
    if word in words[i]:
        print(i)
