'''
    Time Complexity: O(NlogN). N iterations and logN for priority queue
    Space Complexity: O(N). Three arrays and priority queue
    Prim's algorithm is also a greedy algorithm for building a minimum spanning tree in a weighted and undirected graph.
'''

from heapq import heappush, heappop
class Node:
    def __init__(self,v,w) -> None:
        self.__v = v
        self.__w = w
    
    def get_vertex(self):
        return self.__v
    
    def get_weight(self):
        return self.__w
    
    def __lt__(self, next):
        return self.__w < next.__w
    

class Prims:

    def prims(self,adj,n):
        weights = [float('inf')]*n
        parent = [-1]*n
        mst = [False] * n

        weights[0] = 0
        nodes = []
        heappush(nodes, Node(0,0))


        while nodes:
            node = heappop(nodes)
            mst[node.get_vertex()] = True

            for edge in adj[node.get_vertex()]:
                if mst[edge.get_vertex()] == False and weights[edge.get_vertex()]>edge.get_weight():
                    parent[edge.get_vertex()] = node.get_vertex()
                    weights[edge.get_vertex()] = edge.get_weight()
                    heappush(nodes,Node(edge.get_vertex(),edge.get_weight()))

        for i in range(1,n):
            print(parent[i],'->',i)


if __name__=="__main__":
    n = 5
    adj = [[] for i in range(n)]

    adj[0].append(Node(1,2))
    adj[1].append(Node(0,2))

    adj[1].append(Node(2,3))
    adj[2].append(Node(1,3))
		
    adj[0].append(Node(3,6))
    adj[3].append(Node(0,6))

    adj[1].append(Node(3,8))
    adj[3].append(Node(1,8))
		
    adj[1].append(Node(4,5))
    adj[4].append(Node(1,5))

    adj[2].append(Node(4,7))
    adj[4].append(Node(2,7))

    p = Prims()
    p.prims(adj, n)
		
