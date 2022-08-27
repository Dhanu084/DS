# Topological sort can be applied only to Directed Asyclic graph

class Graph:
    def __init__(self, v) -> None:
        self.V = v
        self.graph = [[]for j in range(v+1)]
        self.topo_stack = []
    
    def add_connections(self,u,v):
        if v>self.V or u>self.V:
            return
        
        # self.graph[v].append(u) # commented for directed graph
        self.graph[u].append(v)
    

    def show_graph(self):
        for vertice in self.graph:
            print(vertice)

    def dfs(self, vertice, visited):
        visited[vertice] = True

        for i in self.graph[vertice]:
            if not visited[i]:
                self.dfs(i, visited)
        self.topo_stack.append(vertice) # adding it here so all the vertice gets popped in reverse order


    def topologicalSort(self):
        visited = [False for i in range(self.V+1)]
        
        for i in range(0, self.V+1):
            if not visited[i]:
                self.dfs(i, visited)

        while self.topo_stack:
            print(self.topo_stack.pop())


if __name__=="__main__":
    g = Graph(5)
    # g.add_connections(5,0)
    # g.add_connections(5,2)
    # g.add_connections(4,0)
    # g.add_connections(2,3)
    # g.add_connections(3,1)
    # g.add_connections(4,1)
    # g.topologicalSort()

    g = Graph(4)
    g.add_connections(1,0)
    g.add_connections(2,0)
    g.add_connections(3,1)
    g.add_connections(3,2)
    g.topologicalSort()
