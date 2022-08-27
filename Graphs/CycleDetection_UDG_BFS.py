from collections import deque

class Node:
    def __init__(self, current, parent) -> None:
        self.current = current
        self.parent = parent

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

    def cycleExists(self, vertice, visited):
        queue = deque()
        queue.append(Node(vertice, -1))

        while queue:
            node = queue.popleft()
            visited[node.current] = True
            for i in self.graph[node.current]:
                
                if not visited[i]:
                    queue.append(Node(i, node.current))
                elif i != node.parent:
                    return True
        return False
    
    def bfs(self):
        n = len(self.graph)+1
        visited = [False]*n

        for vertice in range(n-1):
            if not visited[vertice]:
                if self.cycleExists(vertice, visited):
                    return True
        return False
    

if __name__=="__main__":
    g = Graph(11)

    g.add_connections(3,5)
    g.add_connections(5,6)
    g.add_connections(6,7)
    g.add_connections(7,8)
    g.add_connections(8,11)
    g.add_connections(8,9)
    g.add_connections(9,10)
    g.add_connections(10,5)

    g.show_graph()

    print(g.bfs())

    print('*'*50)
    g = Graph(3)
    g.add_connections(1,2)
    g.add_connections(2,3)
    print(g.bfs())