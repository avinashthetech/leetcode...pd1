class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        
         # If there is no edges, just return 0 node since len(edges) == n-1
        if not edges:
            return [0]

        # Intialize a dict to store adjacency list and in-degree for each node
        adj = defaultdict(list)
        inDegree = defaultdict(int)

        # Add all nodes into the two dicts
        for node1, node2 in edges:
            adj[node1].append(node2)
            adj[node2].append(node1)

            inDegree[node1] += 1
            inDegree[node2] += 1

        # Intialize the queue and the visited set
        queue = deque(node for node in adj if inDegree[node] == 1)
        visited = set(queue)

        # Intialize the result
        res = []

        # Iterate until the queue is empty
        while queue:

            # Find the number of nodes at this layer
            n = len(queue)

            # Clear all nodes from the last layer since we haven't reach the center yet
            res.clear()

            # Iterate through all nodes at this layer
            for _ in range(n):

                # Pop a node and add it to the result
                node = queue.popleft()
                res.append(node)

                # Iterate through neighboring nodes
                for neiNode in adj[node]:

                    # If we already visit such node, skip it
                    if neiNode in visited:
                        continue

                    # Else, reduce such node indgree by
                    inDegree[neiNode] -= 1

                    # If such node has in-degree of 1, it will be the most outer node for the next layer
                    if inDegree[neiNode] == 1:

                        # Thus, add such node to the queue and mark it as visited
                        queue.append(neiNode)
                        visited.add(neiNode)

        return res
        