# Topological sort can be applied only to Directed Asyclic graph
from collections import deque

# Kahn's algorithm

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

    def bfs(self, indegree):
        queue = deque()
        for i in range(self.V+1):
            if indegree[i] == 0:
                queue.append(i)

        while queue:
            node = queue.popleft()
            self.topo_stack.append(node)
            for adj_node in self.graph[node]:
                indegree[adj_node]-=1
                if indegree[adj_node] == 0:
                    queue.append(adj_node)

    def topologicalSort(self):
        indegree = [0 for i in range(self.V+1)]

        for v in self.graph:
            for n in v:
                indegree[n]+=1

        self.bfs(indegree)

        print(self.topo_stack)
        # while self.topo_stack:
        #     print(self.topo_stack.pop())


if __name__=="__main__":
    g = Graph(5)
    g.add_connections(5,0)
    g.add_connections(5,2)
    g.add_connections(4,0)
    g.add_connections(2,3)
    g.add_connections(3,1)
    g.add_connections(4,1)
    g.topologicalSort()
