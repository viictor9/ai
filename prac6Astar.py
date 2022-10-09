graph={
    "Oradea":({"Zerind":71,"Sibiu":151},380),
    "Zerind":({"Oradea":71,"Arad":75},374),
    "Arad":({"Zerind":75,"Sibiu":140,"Timisoara":118},399),
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
def get_min(q):
    mn=(0,(0,float("INF")))
    for i in q:
        if sum(q[i])<sum(mn[1]):
            mn=(i,q[i])
            #print(mn)
    return mn[0]

def a_star(graph,prev,dst,path,pcost,q):
    #n:(h(n),g(n)) OF CURRENT VERTEX
    print("Connected Nodes Of Current Node",prev,"with h(n) values:")
    for n in graph[prev][0]: #neighbors list n=Z,S,T
        if n not in path:
            q[n]=(graph[n][1], graph[prev][0][n])
            print(n,"->",q[n])
            add1=sum(q[n])
            path_cost=pcost+add1
            print("A* Value For ",n,"is: ",path_cost)
    while q:
        mn=get_min(q)
        print("Selecting Minimum Vertex: ",mn)
        print("______________________________________________")
        if dst==mn:
            return path+[dst]
        pc=pcost+q[mn][1]
        print("Previous Path Cost:",pc)
        #del q[mn]
        new_path=a_star(graph,mn,dst,path+[mn],pc,q)
        if new_path:
            return new_path
    return []
source=input("Enter Source Vertex:")
dst=input("Enter Destination Vertex:")
heuristic=int(input("Enter Given Heuristic Value for Source:"))
path=a_star(graph,source,dst,[],0,{source:(heuristic,0)})
if path:
    print(path)
else:
    print("Path Not Found")
