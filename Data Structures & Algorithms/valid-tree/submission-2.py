class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        """ 
            Tree:
                1. Connected - Visit all nodes from one
                2. # edges == n - 1
        """
        if not edges: return True

        graph = defaultdict(list)
        numEdges = 0
        nodes = set()
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
            numEdges += 1
            nodes.add(u)
            nodes.add(v)

        numNodes = len(nodes)

        if numNodes - 1 != numEdges:
            return False

        level = deque([edges[0][0]])
        visited = set()
        while level:
            n = len(level)
            for i in range(n):
                node = level.popleft()
                if node in visited:
                    continue
                visited.add(node)
                for neigh in graph[node]:
                    level.append(neigh)
    
        return len(visited) == numNodes