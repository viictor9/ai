import collections
def bfs(graph,root):
    seen,queue=set([root]),collections.deque([root])
    while queue:
        vertex=queue.popleft()
        visit(vertex)
        for node in graph[vertex]:
            if node not in seen:
                seen.add(node)
                queue.append(node)

def allpath(st,end,gr):
    todo=[(st,[st])]
    while len(todo):
        node,path=todo.pop(0)
        for next_node in gr[node]:
            if next_node in path:
                continue
                print('Ideal solution')
            elif next_node==end:
                yield path + [next_node]
            else:
                todo.append((next_node,path + [next_node]))

def visit(n):
    print(n)

def bfs_shortest_path(grah, source, destination):
    checked=[]
    queue=[[source]]
    if source == destination:
        return "SOURCE IS DESTINATION :"
    while queue:
        path=queue.pop(0)
        node=path[-1]
        if node not in checked:
            neighbours = graph[node]
            for neighbour in neighbours:
                new_path=list(path)
                new_path.append(neighbour)
                queue.append(new_path)
                if neighbour == destination:
                    return new_path
            checked.append(node)
    return "PATH DOES NOT EXIST :"

graph={'Oradea': ['Zerind', 'Sibiu'],
       'Zerind':['Oradea', 'Arad'],
       'Arad': ['Zerind','Sibiu','Timisoara'],
       'Timisoara': ['Arad', 'Lugoj'],
       'Lugoj': ['Timisoara', 'Mehadia'],
       'Mehadia': ['Lugoj', 'Drobeta'],
       'Drobeta': ['Mehadia', 'Craiova'],
       'Craiova': ['Drobeta', 'Rimnicu', 'Pitesti'],
       'Pitesti': ['Rimnicu', 'Craiova', 'Bucharest'],
       'Sibiu': ['Oradea', 'Fagaras', 'Rimnicu','Arad'],
       'Fagaras': ['Sibiu', 'Bucharest'],
       'Rimnicu': ['Sibiu', 'Pitesti','Craiova'],
       'Bucharest': ['Urziceni','Giurgiu'],
       'Giurgiu': ['Bucharest'],
       'Urziceni': ['Bucharest', 'Vaslui', 'Hirsova'],
       'Vaslui': ['Lasi', 'Urziceni'],
       'Lasi': ['Neamt', 'Vaslui'],
       'Neamt': ['Lasi'],
       'Hirsova': ['Urziceni', 'Eforie'],
       'Eforie': ['Hirsova']
       }

print("GRAPH TRAVERSAL: ")
bfs(graph,'Arad')
print('\n\nall paths is')
[print (x) for x in allpath ('Arad','Bucharest', graph)]
print("\n SHORTERT PATH OF GARPH IS: : ", bfs_shortest_path(graph, 'Arad','Bucharest'))
