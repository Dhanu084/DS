from collections import defaultdict
# form topstack
# pop from topo stack and update distance

class Node:
    def __init__(self, v, w) -> None:
        self.v = v
        self.w = w
class Graph:

    def __init__(self, n) -> None:
        self.adj = defaultdict(list)
        self.n = n
        self.distance = [float('inf')]*n
        self.topoStack = []
    
    def addEdge(self, u, v, w):
        self.adj[u].append(Node(v, w))

    def topologicalSort(self,vertice, visited):
        visited.add(vertice)

        for nei in self.adj.get(vertice, []):
            if nei.v not in visited:
                visited.add(nei.v)
                self.topologicalSort(nei.v, visited)
        self.topoStack.append(vertice)

    def dfs(self):
        visited = set()

        for i in range(self.n):
            if not i in visited:
                self.topologicalSort(i, visited)
    
    def shortestPath(self, start):
        #1 form topologic stack
        #2 perfrom bfs popping from toplogical Sort and upadte distance array
        self.distance[start] = 0
        while self.topoStack:
            node = self.topoStack.pop()
            if self.distance[node]!=float('inf'):
                for nei in self.adj[node]:
                    if self.distance[nei.v] > self.distance[node]+nei.w:
                        self.distance[nei.v] = self.distance[node]+nei.w
        return self.distance


    def printGraph(self):
        for i in range(len(self.adj)):
            print(self.adj.get(i))
    

if __name__=="__main__":
    g = Graph(6)

    g.addEdge(0,1,2)
    g.addEdge(0,4,1)
    g.addEdge(1,2,3)
    g.addEdge(4,2,2)
    g.addEdge(2,3,6)
    g.addEdge(4,5,4)
    g.addEdge(5,3,1)
    # print(g.adj)
    # g.printGraph()
    g.dfs()
    print(g.topoStack)
    print(g.shortestPath(0))