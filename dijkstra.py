#! /usr/bin/python

def display(s):
    for row in s:
        print s[row]
        print

def get_min_node(univisited_map, dist):
    min_node = None
    min_dist = float('inf')
    for v in univisited_map:
        if dist[v] < min_dist:
            min_node = v
    return min_node

def get_neighbour(graph, node):
    l = []
    for i in graph[node]:
        if (graph[node][i] != float('inf')) and i != node:
            l.append(i)
    return l


def dijkstra(graph, src):
    dist = {}
    prev = {}
    unvisited = {}
    for v in graph:
        if v == src:
            dist[v] = 0
        else:
            dist[v] = float('inf')
        prev[v] = None
        unvisited[v] = 1

    while unvisited:
        node = get_min_node(unvisited, dist) #which is still a char like 'a' or 'c'
        del unvisited[node]

        neighbours = get_neighbour(graph, node)
        for neighbour in neighbours:
            new_dist = dist[node] + graph[node][neighbour]
            if new_dist < dist[neighbour]:
                dist[neighbour] = new_dist
                prev[neighbour] = node
    return prev

def get_shortest_path(prev, dst):
    path = []
    cur = dst
    path.insert(0, cur)
    while cur:
        path.insert(0,cur)
        cur = prev[cur]
    return path



def main():
    number_of_nodes = 6
    graph = {}
    populate(graph, number_of_nodes)
    display(graph)
    prev = dijkstra(graph, 'a')
    print 'prev=',prev
    dst = 'f'
    paths = get_shortest_path(prev, dst)
    print paths



def populate(graph, number_of_nodes):
    for i in range(number_of_nodes):
        x = chr(ord('a') + i)
        graph[x] = {}
        for j in range(number_of_nodes):
            y = chr(ord('a') + j)
            graph[x][y] = {}

    graph['a']['a'] = 0
    graph['a']['b'] = 4
    graph['a']['c'] = 2
    graph['a']['d'] = float('inf')
    graph['a']['e'] = float('inf')
    graph['a']['f'] = float('inf')

    graph['b']['a'] = 4
    graph['b']['b'] = 0
    graph['b']['c'] = 1
    graph['b']['d'] = 5
    graph['b']['e'] = float('inf')
    graph['b']['f'] = float('inf')

    graph['c']['a'] = 2
    graph['c']['b'] = 1
    graph['c']['c'] = 0
    graph['c']['d'] = 8
    graph['c']['e'] = 10
    graph['c']['f'] = float('inf')

    graph['d']['a'] = float('inf')
    graph['d']['b'] = 5
    graph['d']['c'] = 8
    graph['d']['d'] = 0
    graph['d']['e'] = 2
    graph['d']['f'] = 6

    graph['e']['a'] = float('inf')
    graph['e']['b'] = float('inf')
    graph['e']['c'] = 10
    graph['e']['d'] = 2
    graph['e']['e'] = 0
    graph['e']['f'] = 3

    graph['f']['a'] = float('inf')
    graph['f']['b'] = float('inf')
    graph['f']['c'] = float('inf')
    graph['f']['d'] = 6
    graph['f']['e'] = 3
    graph['f']['f'] = 0


if __name__ == '__main__':
    main()