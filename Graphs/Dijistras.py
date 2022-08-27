from heapq import heappush, heappop

# TC - O(N+E) * logN
# SC - O(N)+O(N)+(N)

class Node:
    def __init__(self, v , weight) -> None:
        self.v = v
        self.w = weight

    def __lt__(self,nxt):
        return self.w < nxt.w


class Dijistras:
    def shortesPath(self,start,adj, n):
        distance = [float('inf')]*n
        distance[start] = 0

        nodes = []
       
        heappush(nodes,Node(start, 0))

        while nodes:
            node = heappop(nodes)

            for nei in adj[node.v]:
                if distance[nei.v] > distance[node.v]+ nei.w:
                    distance[nei.v] = distance[node.v] + nei.w
                    heappush(nodes, Node(nei.v, distance[nei.v]))
        
        for dist in distance:
            print(dist, end=' ')

if __name__=="__main__":
    n = 5

    adj = [[]for i in range(n)]
    adj[0].append(Node(1,2))
    adj[1].append(Node(0,2))

    adj[1].append(Node(2, 4))
    adj[2].append(Node(1, 4))

    adj[0].append(Node(3,1))
    adj[3].append(Node(0,1))

    adj[3].append(Node(2,3))
    adj[2].append(Node(3,3))

    adj[1].append(Node(4,5))
    adj[4].append(Node(1,5))

    adj[2].append(Node(4,1))
    adj[4].append(Node(2,1))

    dijistras = Dijistras()
    dijistras.shortesPath(0,adj, n)