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
start=input("Enter Source Node:")
des=input("Enter Destination Node:")
def dfs(g,start,li,des):
    
    if start not in li:
        li.append(start)
        for i in g[start]:
            if li[-1] is des:
                break
            dfs(g,i,li,des)
    return li
print(dfs(graph,start,[],des))
