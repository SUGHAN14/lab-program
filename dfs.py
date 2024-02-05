graph = {
    '5': ['3', '7'],
    '3': ['2', '4'],
    '7': ['8'],
    '2': [],
    '4': ['8'],
    '8': []
}
visited=[]
def dfs(visited,graph,node):
    if node not in visited:
        print(node)
        visited.append(node)
        for neighbours in graph[node]:
            dfs(visited,graph,neighbours)
print("Following is the depth-first search:")
dfs(visited,graph,'5')
