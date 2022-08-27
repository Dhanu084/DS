from collections import deque
from typing import List
# finding distance from 0 to all other nodes
def bfs(adj: List[List[int]] ,N: int,src: int):
    distance = [float('inf')]*(N)
    distance[src] = 0

    queue = deque()
    queue.append(src)

    while queue:
        node = queue.popleft()
        for v in adj[node]:
            if distance[node]+1<distance[v]:
                distance[v] = distance[node]+1
                queue.append(v)
    print(distance)

if __name__ == "__main__":
    adj = [
        [1,3],
        [0,2,3],
        [1,6],
        [0,4],
        [3,5],
        [4,6],
        [2,5,7,8],
        [6,8],
        [6,7]
    ]
    bfs(adj=adj, N=len(adj), src=0)