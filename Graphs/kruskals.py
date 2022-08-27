'''
Sort all edges sorted by weight
Greedily pick shortest edge
Connect two components using Union Rank and Path Compression
Time Complexity: O(ElogE)+O(E*4*alpha), ElogE for sorting and E*4*alpha for findParent operation ‘E’ times
Kruskal's algorithm is a greedy algorithm for building a minimum spanning tree in a weighted and undirected graph.

Space Complexity: O(N). Parent array+Rank Array
'''

class Node:
    def __init__(self, u, v, w) -> None:
        self.u, self.v, self.w = u, v, w
    def __lt__(self, next):
        return self.w<next.w
    

class Kruskals:

    def findParent(self, vertice, parent):
        if vertice == parent[vertice]:
            return vertice
        
        parent[vertice] = self.findParent(parent[vertice], parent)
        return parent[vertice]

    def union(self, u, v, parent, rank):
        if rank[u]>rank[v]:
            parent[v] = u
        elif rank[u]<rank[v]:
            parent[u] = v
        else:
            parent[v] = u
            rank[u]+=1
    
    def Kruskal(self, adj, n):
        parent = [i for i in range(0,n+1)]
        rank = [0 for i in range(0, n+1)]

        adj.sort()

        mstCost = 0
        mst = []

        for edge in adj:
            if self.findParent(edge.u, parent)!=self.findParent(edge.v, parent):
                mstCost+=edge.w
                mst.append(edge)
                self.union(edge.u, edge.v, parent, rank)
        print(mstCost)
        for m in mst:
            print(m.u,'->', m.v)

if __name__=="__main__":
    n = 5
    adj = []

    adj.append(Node(0,1,2))
    adj.append(Node(1,2,3))
    adj.append(Node(0,3,6))
    adj.append(Node(1,3,8))
    adj.append(Node(1,4,5))
    adj.append(Node(2,4,7))

    k = Kruskals()
    k.Kruskal(adj, n)