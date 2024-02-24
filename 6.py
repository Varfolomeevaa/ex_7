def distance(s, f, graph):
    dst = 0
    for m in range(number_city):
        if graph[s][m][0] == f:
            dst = graph[s][m][1]
    return dst


number_city = int(input())
number_roads = int(input())
gr = {}

for i in range(number_roads):
    ptr = input().split()
    if ptr[0] not in gr:
        gr[ptr[0]] = [[ptr[1], int(ptr[2])]]

    else:
        gr[ptr[0]].append([ptr[1], int(ptr[2])])
    if ptr[1] not in gr:
        gr[ptr[1]] = [[ptr[0], int(ptr[2])]]

    else:
        gr[ptr[1]].append([ptr[0], int(ptr[2])])

for i in gr:
    cities = []
    for j in range(len(gr[i])):
        cities.append(gr[i][j][0])
    for k in gr:
        if k not in cities:
            gr[i].append([k, float('inf')])

for k in gr:
    for i in gr:
        for j in range(number_city):
            dist_1 = gr[i][j][1]
            dist_2 = distance(i, k, gr)
            dist_3 = distance(k, gr[i][j][0], gr)
            if dist_2 + dist_3 < dist_1:
                gr[i][j][1] = dist_2 + dist_3

cities = input().split()
print(distance(cities[0], cities[1], gr))
