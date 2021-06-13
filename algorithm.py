import re


# Парсинг файлов
def parse_file(file_name, dic):
    with open(file_name, 'r') as f:
        graph_str = f.readline()

    tuples_array_str = re.findall(r"\((\d+, \d+)\)", graph_str)
    edge_count = len(tuples_array_str)
    for el in tuples_array_str:
        el = el.split(', ')
        if int(el[0]) not in dic:
            dic[int(el[0])] = []
        if int(el[1]) not in dic:
            dic[int(el[1])] = []
        dic[int(el[0])].append(int(el[1]))
        dic[int(el[1])].append(int(el[0]))

    return edge_count


# Поиск в глубину
def depth_search(graph, v, num, father, T):
    i = 1
    S = []
    S.append(v)
    while len(S) != 0:
        v = S.pop()
        num[v] = i
        i += 1
        for u in graph[v]:
            if num[u] == 0:
                T.append((u, v))
                father[u] = v
                S.append(u)


# Проверка на двудольность (рекурсивый поиск в глубину)
def is_graph_bipartite(graph, v, visited, set1, set2):
    if v in set2:
        return False
    if v not in visited:
        visited.append(v)
        set1.add(v)
        for node in graph[v]:
            is_graph_bipartite(graph, node, visited, set2, set1)
    return True


# Поиск обратных ребер
def find_B(graph, father, B):
    for son in father:
        for incident_node in graph[son]:
            if (incident_node != father[son]
               or (incident_node in father
               and father[incident_node] != son)):
                B.append((incident_node, son))


# Точка входа программы
def main(node_count, input_file, output_T_file, output_B_file):
    graph = {}
    edge_count = parse_file(input_file, graph)

    v = list(graph.keys())[0]
    num = [0] * node_count
    father = {}
    T = []
    depth_search(graph, v, num, father, T)

    B = []
    find_B(graph, father, B)

    is_graph_connected = 0 not in num
    print(input_file)
    if is_graph_connected:
        print("Граф связен")
    else:
        print("Граф не связен")

    if is_graph_connected and node_count - 1 == edge_count:
        print("Граф является деревом")
    else:
        print("Граф не является деревом")

    if is_graph_bipartite(graph, v, [], set(), set()):
        print("Граф двудольный")
    else:
        print("Граф не двудольный")

    with open(output_T_file, 'w') as f:
        f.write(str(T))

    with open(output_B_file, 'w') as f:
        f.write(str(B))

    print()


if __name__ == "__main__":
    main(100, "./input/graph1.txt", "./output/T1.txt", "./output/B1.txt")
    main(53, "./input/graph2.txt", "./output/T2.txt", "./output/B2.txt")
