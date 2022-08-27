from collections import defaultdict
'''
Bellman ford algorithm is used to detect negative cycle in a graph
it is only used to detect the cycle not find shortest path
For unidrected graph , convert it into directed graph with same weight
Steps:
Relax N-1 for every edges
distance[currnode]+currentweight<distance[vnode]: distance[vnode] = distance[currnode]+currentweight
TC: O(N-1)*E
SC: O(N)
'''
class Node:
    def __init__(self, u,v,w) -> None:
        self.u, self.v, self.w = u, v, w
    
    def getU(self):return self.u
    def getV(self):return self.v
    def getW(self):return self.w

class BellmanFord:
    def __init__(self, n):
        self.n = n
        self.distance = [float('inf')] * (n+1)
        self.edges = []

    def addEdge(self, u, v, w):
        node = Node(u,v,w)
        self.edges.append(node)

    def main(self, src):
        self.distance[src] = 0
        for i in range(1, self.n):
            for nei in self.edges:
                if self.distance[nei.getU()] + nei.getW() < self.distance[nei.getV()]:
                    self.distance[nei.getV()] = self.distance[nei.getU()] + nei.getW()
        print(self.distance)

        isCycle = False
        for nei in self.edges:
            if self.distance[nei.getU()] + nei.getW() < self.distance[nei.getV()]:
                isCycle = True
                break
        if isCycle:print('Cycle Exists')
        else: print('No Cycle')


if __name__ == "__main__":
    b = BellmanFord(5)
    b.addEdge(0,1,5)
    b.addEdge(1,2,-2)
    b.addEdge(1,5,-3)
    b.addEdge(2,4,3)
    b.addEdge(5,3,1)
    b.addEdge(3,2,6)
    b.addEdge(3,4,-2)
    b.main(0)


    