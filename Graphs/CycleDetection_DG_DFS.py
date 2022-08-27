class Graph:
    def __init__(self, v) -> None:
        self.V = v
        self.graph = [[]for j in range(v+1)]
    
    def add_connections(self,u,v):
        if v>self.V or u>self.V:
            return
        
        # self.graph[v].append(u) # commented for directed graph
        self.graph[u].append(v)
    

    def show_graph(self):
        for vertice in self.graph:
            print(vertice)

    
    def cycleExists(self, vertice, visited, dfsVisit):
        visited[vertice] = True
        dfsVisit[vertice] = True

        for i in self.graph[vertice]:
            if dfsVisit[i]:
                return True
            if not visited[i]:
                if self.cycleExists(i, visited, dfsVisit):
                    return True
        dfsVisit[vertice] = False

    def dfs(self):
        n = len(self.graph)
        visited = [False]*n
        dfsVisit = [False]*n

        for i in range(1,n):
            if not visited[i]:
                if(self.cycleExists(i, visited, dfsVisit)):
                    return True
        return False




if __name__ == "__main__":
    g = Graph(9)
    g.add_connections(1,2)
    g.add_connections(2,3)
    g.add_connections(3,5)
    g.add_connections(4,5)
    g.add_connections(3,6)
    g.add_connections(6,5)
    g.add_connections(7,2)
    g.add_connections(7,8)
    g.add_connections(8,9)
    g.add_connections(9,7)

    g.show_graph()
    print(g.dfs())