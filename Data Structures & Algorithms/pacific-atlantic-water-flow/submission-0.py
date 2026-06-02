class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        n, m = len(heights), len(heights[0])
        directions = ((1,0),(0,1),(-1,0),(0,-1))
        def bfs(origin):
            level = deque([origin])
            visited = set()
            pac, at = False, False
            while level:
                num = len(level)
                prev = None
                for i in range(num):
                    node = level.popleft()
                    x, y = node

                    if (x, y) in visited:
                        continue
                    
                    visited.add((x,y))

                    if x == 0 or y == 0:
                        pac = True
                    
                    if x == n - 1 or y == m - 1:
                        at = True
                    
                    for direction in directions:
                        new_x = x + direction[0]
                        new_y = y + direction[1]

                        if new_x < 0 or new_x >= n or new_y < 0 or new_y >= m:
                            continue

                        if heights[new_x][new_y] <= heights[x][y]:
                            level.append((new_x, new_y))
        
            return (pac, at)

        ret = []
        for i in range(n):
            for j in range(m):
                pac, at = bfs((i ,j))
                if pac and at:
                    ret.append([i, j])
                
        return ret