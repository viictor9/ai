graph={
    'Oradea': ['Zerind', 'Sibiu'],
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
def dls(s,g,path,level,max_depth):
    print("Current Level is:",level)
    print("Testing for",g+" "+"Node from",s)
    path.append(s)
    e="Max Depth Limit Reached!"
    while True:
        if level>max_depth:
            print("Current Level Reaches Maximum Depth")
            return False
            break
        if s==g:
            print("Goal Node Found!")
            return path
        print("Goal Node Test Failed!")
        print("Expanding Current Node",s)
        print("--------------------------------------")
        for neighbor in graph[s]:
            if dls(neighbor,g,path,level+1,max_depth):
                return path
                path.pop()
                return False
            return False

s=input("Enter Source Node:")
g=input("Enter Goal Node:")
max_depth=int(input("Enter Maximum Depth Limit:"))
print()
path=list()
output=dls(s,g,path,0,max_depth)
if (output):
    print("There Exists a path from source to goal")
    print("Path is:",path)
else:
    print("No Path From Source to Goal in given depth Limit")
