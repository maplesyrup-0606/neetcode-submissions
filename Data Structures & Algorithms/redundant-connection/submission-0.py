class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        mp = defaultdict(list)
        nodes = set()
        for u, v in edges:
            mp[u].append(v)
            mp[v].append(u)
            nodes.add(u)
            nodes.add(v)

        def traverse(mp, x, y):
            visited = set()

            level = deque([x])

            while level:
                n = len(level)

                for i in range(n):
                    node = level.popleft()
                    if node in visited:
                        continue
                    visited.add(node)
                    
                    neighbors = mp[node]

                    for neigh in neighbors:
                        if (node == x and neigh == y) or (node == y and neigh == x):
                            continue
                        level.append(neigh)
                        
            return visited

        res = []
        for u, v in edges:
            print(traverse(mp, u, v))
            if len(nodes) == len(traverse(mp, u, v)):
                res.append([u, v])
        
        for i in range(len(edges) - 1, -1, -1):
            if edges[i] in res:
                return edges[i]