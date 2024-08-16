def serch_the_path(graph, start, current, path, all_paths):
    path.append(current)
    if current == start and len(path) > 1:
        all_paths.append(path)
        return
    if current not in graph:
        all_paths.append(path)
        return
    for node in graph[current]:
        if node not in path or node == start:  
            serch_the_path(graph, start, node, path[:], all_paths)

    all_paths.append(path)

def find_all_paths(graph):
    all_paths = []
    for start_node in graph:
        serch_the_path(graph, start_node, start_node, [], all_paths)
    return all_paths   

def find_longest_path(paths,weighted_graph):
    longest = 0
    for i in paths:
        weight = 0
        for j in range(len(i)-1):
            for k in weighted_graph:
                if i[j] == k:
                    for l in weighted_graph[k]:
                        if i[j+1] == l[0]:
                            weight += l[1]
        weight = round(weight,2)
        if longest < weight:
            longest = weight
            result = []
            result.append(i)
        elif longest == weight:
            result.append(i)
    return longest,result
input_data = []
weighted_graph = {}
graph = {}

while True:
    line = input("始点,終点,距離を入力してください(空白で入力終了)")
    if line:
        input_data.append([int(x) if x.isdigit() else float(x) for x in line.split(", ")])
    else:
        break
for i in input_data:
    if i[0] not in graph:
        weighted_graph[i[0]] = []
        graph[i[0]] = []
    weighted_graph[i[0]].append([i[1], i[2]])
    graph[i[0]].append(i[1])
 
paths = find_all_paths(graph)
distance,result = find_longest_path(paths,weighted_graph)
print(f"最大の距離:{distance}\n経路:{result}")