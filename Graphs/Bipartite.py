from collections import deque


class Graph:
    def __init__(self, v) -> None:
        self.V = v
        self.graph = [[]for j in range(v+1)]
    
    def add_connections(self,v, u):
        if v>self.V or u>self.V:
            return
        
        self.graph[v].append(u)
        self.graph[u].append(v)
    

    def show_graph(self):
        for vertice in self.graph:
            print(vertice)

    def __bfs_check_bipartite(self, vertice, colors):
       
        queue = deque()
        queue.append(vertice)
        colors[vertice] = 1
        while queue:
            node = queue.popleft()
            for i in self.graph[node]:
                if colors[i] == -1:
                    colors[i] = 1-colors[node]
                    queue.append(i)
                elif colors[i] == colors[node]:
                    return False
        return True


    def bfs(self):
        colors = [-1 for i in range(self.V+1)]
        for i in range(1,self.V+1):
            if colors[i] == -1:
                if not self.__bfs_check_bipartite(i, colors):
                    return False
        
        return True

    def __dfs_check_bipartite(self, vertice, colors):
        if colors[vertice] == -1:
            colors[vertice] = 1
        
        for i in self.graph[vertice]:
            if colors[i] == -1:
                colors[i] = 1 - colors[vertice]
                if not self.__dfs_check_bipartite(i, colors):
                    return False
            elif colors[i] == colors[vertice]:
                return False
        return True

    def dfs(self):
        colors = [-1 for i in range(self.V+1)]
        for i in range(1, self.V+1):
            if colors[i] == -1:
                if not self.__dfs_check_bipartite(i, colors):
                    return False
        return True

if __name__ == "__main__":
    g = Graph(5)

    g.add_connections(1,2)
    g.add_connections(1,4)
    g.add_connections(2,3)
    g.add_connections(4,5)

    # g.show_graph()
    # print(g.bfs())
    print(g.dfs())

    g.add_connections(1,2)
    g.add_connections(1,5)
    g.add_connections(2,3)
    g.add_connections(3,4)
    g.add_connections(4,5)

    # print(g.bfs())
    print(g.dfs())