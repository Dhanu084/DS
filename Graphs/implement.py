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

    def __bfs_helper(self, node, visited):
        queue = deque()
        queue.append(node)
        visited[node] = True
        while queue:
            current_node = queue.popleft()
            print(current_node, end='->')
            for v in self.graph[current_node]:
                if not visited[v]:
                    queue.append(v)
                    visited[v] = True
                    
        print()

    def bfs(self):
        visited = [False for i in range(self.V+1)]
        for i in range(1, self.V):
            if not visited[i]:
                self.__bfs_helper(i, visited)


    def __dfs_helper(self, node, visited):
        if visited[node]:
            return
        print(node,end='->')
        visited[node] = True
        for i in self.graph[node]:
            if not visited[i]:
                self.__dfs_helper(i, visited)
        print()
            

    
    def dfs(self):
        visited = [False for i in range(self.V+1)]
        for i in range(1,self.V+1):
            if not visited[i]:
                self.__dfs_helper(i, visited)
        


if __name__=="__main__":
    g = Graph(7)

    g.add_connections(0,2)
    g.add_connections(0,5)
    g.add_connections(2,4)
    g.add_connections(1,6)
    g.add_connections(5,4)
    # g.add_connections(5,7)



    g.show_graph()
    # g.bfs()
    g.dfs()