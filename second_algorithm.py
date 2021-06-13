import re


# Парсинг файлов
def parse_file(lst = {}):
    with open("./input/graph2.txt", 'r') as f:
        graph_str = f.readline()

    tuples_array_str = re.findall(r"\((\d+, \d+)\)", graph_str)
    for el in tuples_array_str:
        el = el.split(', ')
        if int(el[0]) not in lst:
            lst[int(el[0])] = []
        if int(el[1]) not in lst:
            lst[int(el[1])] = []
        lst[int(el[0])].append(int(el[1]))
        lst[int(el[1])].append(int(el[0]))

    return lst


# Поиск точек сочленения и блоков
def BiComp(v):
    global i
    num[v] = i
    L[v] = i
    i += 1
    for u in lst[v]:
        if num[u] == 0:
            SE.append((u, v))
            father[u] = v
            BiComp(u)
            L[v] = min(L[v], L[u])
            if L[u] >= num[v]:
                dots.append(v)
                block = []
                for edge in reversed(SE):
                    block.append(SE.pop())
                    if ((edge[0] == u and edge[1] == v)
                       or (edge[0] == v and edge[1] == u)):
                        break
                blocks.append(block)
        elif num[u] < num[v] and u != father[v]:
            SE.append((v, u))
            L[v] = min(L[v], num[u])


lst = parse_file()

i = 1
SE = []
father = {}
L = {}
num = [0] * (max(lst) + 1)

v = 6
father[v] = 0

blocks = []
dots = []

BiComp(v)
dots.pop()
dots = list(set(dots))


with open("./output/V.txt", 'w') as f:
    f.write(str(dots))

with open("./output/Blocks.txt", 'w') as f:
    f.write(str(blocks))
