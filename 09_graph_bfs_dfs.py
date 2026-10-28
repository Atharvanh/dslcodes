from collections import deque

def bfs(graph, start):
    visited = {start}
    queue = deque([start])
    order = []
    while queue:
        node = queue.popleft()
        order.append(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return order

def dfs(matrix, names, start):
    visited = [False] * len(names)
    order = []
    def visit(node):
        visited[node] = True
        order.append(names[node])
        for neighbor in range(len(names)):
            if matrix[node][neighbor] and not visited[neighbor]:
                visit(neighbor)
    visit(names.index(start))
    return order

def main():
    names = input('Enter unique location names separated by spaces: ').split()
    if not names or len(set(names)) != len(names):
        print('Enter at least one location, with no duplicates')
        return
    graph = {name: [] for name in names}
    matrix = [[0] * len(names) for name in names]
    for i in range(int(input('Number of undirected routes: '))):
        route = input('Enter two connected locations: ').split()
        if len(route) != 2 or any(name not in graph for name in route):
            print('Invalid route')
            continue
        a, b = route
        if b not in graph[a]:
            graph[a].append(b)
            graph[b].append(a)
        x, y = names.index(a), names.index(b)
        matrix[x][y] = matrix[y][x] = 1
    start = input('Starting location: ')
    if start not in graph:
        print('Location not found')
        return
    print('Adjacency list:', graph)
    print('Adjacency matrix in location order:', names)
    for row in matrix:
        print(row)
    print('BFS:', bfs(graph, start))
    print('DFS:', dfs(matrix, names, start))
    print('Only locations reachable from the start are visited')

if __name__ == '__main__':
    main()
