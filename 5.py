def kids(name_par):
    kid = tree.get(name_par, 0)
    if kid == 0:
        return 0
    summ = len(kid)
    for j in range(len(kid)):
        summ += kids(kid[j])
    return summ


number = int(input())
tree = {}

for i in range(number):
    ptr = input().split()
    if ptr[0] not in tree:
        tree[ptr[0]] = [ptr[1]]
    else:
        tree[ptr[0]].append(ptr[1])

name = input()

print(kids(name))
