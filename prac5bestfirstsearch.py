graph={
    "Oradea":({"Zerind":71,"Sibiu":151},380),
    "Zerind":({"Oradea":71,"Arad":75},374),
    "Arad":({"Zerind":75,"Sibiu":140,"Timisoara":118},366),
    "Timisoara":({"Arad":118,"Lugoj":111},329),
    "Lugoj":({"Timisoara":111,"Mehadia":70},244),
    "Mehadia":({"Lugoj":70,"Drobeta":75},241),
    "Sibiu":({"Oradea":151,"Fagaras":99,"Rimnicu":80,"Arad":140},253),
    "Fagaras":({"Sibiu":99,"Bucharest":211},176),
    "Rimnicu":({"Sibiu":80,"Pitesti":97,"Craiova":146},193),
    "Bucharest":({"Fagaras":211,"Pitesti":101,"Urziceni":85,"Giurgiu":90},0),
    "Pitesti":({"Rimnicu":97,"Craiova":138,"Bucharest":101},100),
    "Craiova":({"Rimnicu":146,"Pitesti":138,"Drobeta":128},160),
    "Drobeta":({"Mehadia":75,"Craiova":120},242),
    "Urziceni":({"Bucharest":85,"Vaslui":142,"Hirsova":98},80),
    "Giurgiu":({"Bucharest":90},77),
    "Vaslui":({"Lasi":92,"Urziceni":142},199),
    "Hirsova":({"Urziceni":98,"Eforie":86},151),
    "Lasi":({"Vaslui":92,"Neamt":87},226),
    "Eforie":({"Hirsova":86},161),
    "Neamt":({"Lasi":87},234)
    }
def greedy_search_rec(graph,prev,dst,path,q):
    #n:(h(n))
    print("Connnected Nodes of Current Node",prev,"with h(n) values: ")
    #This loop is for Traversing Each Node and Take it's Heuristic Value
    for n in graph[prev][0]:#neighbours list prev=arad,->z,s,t
        if n not in path:
            q[n]=graph[n][1]#dictionary to store the nodes
            print(n,"->",q[n])
    #This Loop is used for traversing the nodes in the dictionary 
    while q:
        mn=min(q,key=q.get)
        print("Taking Minimum h(n) vertex: ",mn)
        #print mn
        if dst==mn:
            return path+[dst]
        #del q[mn]
        new_path=greedy_search_rec(graph,mn,dst,path+[mn],q)
        if new_path:
            return new_path
    return[]
source=input("Enter Source Vertex: ")
dest=input("Enter Destination Vertex: ")
path=greedy_search_rec(graph,source,dest,[source],{})
if path:
    print(path)
else:
    print("Path Not Found!")
