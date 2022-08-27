from collections import defaultdict
'''
Josaraju's algorithm to find strongly connected components for directed graphs
1 - Sort according to finishing time  i.e Topological sort
2 - Transpose the edges i.e changed direction of edges
3 - DFS by popping from toplogical stack

Strongly Connected Components -> a part of graph in which all nodes are reachable by every other node
'''
class Kosaraju:

    def __init__(self, n) -> None:
        self.adj = defaultdict(list)
        self.n = n

    def addEdge(self, u, v):
        self.adj[u].append(v)
    
    def createTopoStack(self, vertice, stack, visited):
        visited.add(vertice)

        for nei in self.adj.get(vertice, []):
            if nei not in visited:
                self.createTopoStack(nei, stack, visited)
        stack.append(vertice)
    
    def transposeAdjacencyList(self):
        transposeAdj = {}
        for i in range(1,self.n+1):
            for edge in self.adj.get(i,[]):
                if edge not in transposeAdj:
                    transposeAdj[edge] = []
                transposeAdj[edge].append(i)
        return transposeAdj

    def dfs(self, vertice, visited, current):
        visited.add(vertice)
        current.append(vertice)
        for nei in self.adj.get(vertice,[]):
            if nei not in visited:
                self.dfs(nei, visited, current)

    
    def main(self):
        visited = set()
        topoStack = []
        for i in range(1,self.n+1):
            if i not in visited:
                self.createTopoStack(i, topoStack, visited)

        self.adj = self.transposeAdjacencyList()
        visited = set()

        output = []

        while topoStack:
            vertice = topoStack.pop()
            current = []
            if vertice not in visited:
                self.dfs(vertice, visited, current)
                output.append(current)
        return output


if __name__=="__main__":
    k = Kosaraju(5)
    k.addEdge(1, 2)
    k.addEdge(2, 3)
    k.addEdge(3, 1)
    k.addEdge(2, 4)
    k.addEdge(4, 5)

    print(k.main())
        
