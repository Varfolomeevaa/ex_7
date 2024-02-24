number = int(input())
words = {}

for i in range(number):
    ptr = input().split()
    words[ptr[0]] = ptr[1]

ptr_old = input().split()
ptr_new = ''

for i in range(len(ptr_old)):
    ptr_new += words.get(ptr_old[i], ptr_old[i]) + ' '

print(ptr_new)
