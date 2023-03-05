def depthFirstSearch(visited, graph, node):
    global order
    if node not in visited:
        visited.add(node)
        for at in graph[node]:
            depthFirstSearch(visited, graph, at)
        order.insert(0, node)


visited = set()
order = []
dependencies = []
graph = dict()

# read input and add dependencies to the list.
with open('input.txt') as file:
    for line in file:
        line1 = line.strip()
        if len(line1) > 0:
            d = (line1[:6], line1[9:])
            dependencies.append(d)

# create a directed graph of dependencies.
for task in dependencies:
    if task[0] not in graph:
        graph[task[0]] = []
    if task[1] not in graph:
        graph[task[1]] = []
    graph[task[0]].append(task[1])

# run dfs on each node in the graph.
for at in graph.keys():
    depthFirstSearch(visited, graph, at)

# write output to a text file.
with open('200088D.txt', 'w') as output:
    string = ''
    for task in order:
        string += task + ','
    string = string.strip(',')
    output.write(string)
