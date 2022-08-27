from collections import deque

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

    def cycleExists(self,indegree):
        queue = deque()

        for indeg in indegree:
            if indeg == 0:
                queue.append(indeg)
        count = 0
        while queue:
            node = queue.popleft()
            count+=1

            for nei in self.graph[node]:
                indegree[nei]-=1
                if indegree[nei] == 0:
                    queue.append(nei)
        
        return count == self.V
    
    def toposort(self):
        indegree = [0]*(self.V+1)

        for i in range(self.V+1):
            for nei in self.graph[i]:
                indegree[nei]+=1

        if not self.cycleExists(indegree):
            return True




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
    print(g.toposort())
