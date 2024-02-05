graph = {
    '5': ['3', '7'],
    '3': ['2', '4'],
    '7': ['8'],
    '2': [],
    '4': ['8'],
    '8': []
}

visited = []  # Use a set for efficiency
queue = []

def bfs(visited, graph, node):
    visited.append(node)  # Use add() for sets
    queue.append(node)

    while queue:
        current_node = queue.pop(0)
        print(current_node, end=" ")

        for neighbour in graph[current_node]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)

print("Following is the breadth-first search:")
bfs(visited, graph, '5')
