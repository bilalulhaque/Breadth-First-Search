#Breadth First Search
import copy
graph = {
    'A':['B','D'],
    'B':['C','E'],
    'C':[],
    'D':['E','G','H'],
    'E':['C','F'],
    'F':[],
    'G':['H'],
    'H':[]
}

def bfs(startNode,finalNode):
    path=[]
    queue=[]
    queue.append([startNode])

    while len(queue)>0:
        path.append(queue.pop(0))
        node=path[-1][-1]

        for neighbor in graph[node]:
            newPath=copy.deepcopy(path[-1])
            if neighbor == finalNode:
                finalPath=copy.deepcopy(path[-1])
                finalPath.append(finalNode)
                print("Final Path", finalPath)
                return "Found Goal Node"
            newPath.append(neighbor)
            queue.append(newPath)

            print("Path", path)
            print("Queue", queue)
bfs('A','G')