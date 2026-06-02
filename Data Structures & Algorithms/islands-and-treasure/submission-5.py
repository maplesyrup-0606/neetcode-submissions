class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        water = -1
        treasure = 0
        land = 2 ** 31 - 1

        n, m = len(grid), len(grid[0])
        directions = ((1,0),(0,1),(-1,0),(0,-1))
        
        def bfs(origin):
            level = deque([origin])
            visited = set()
            num = 0
            while level:
                nodes = len(level)
                for i in range(nodes):
                    x, y = level.popleft()

                    if x < 0 or x >= n or y < 0 or y >= m:
                        continue

                    if (x, y) in visited: continue

                    visited.add((x,y))

                    if grid[x][y] == water:
                        continue

                    if grid[x][y] == treasure:
                        grid[origin[0]][origin[1]] = num
                        return
                    
                    for direction in directions:
                        new_x = x + direction[0]
                        new_y = y + direction[1]
                        level.append((new_x, new_y))
                
                num += 1
            return 

        for i in range(n):  
            for j in range(m):
                if grid[i][j] == land:
                    bfs((i,j))
        
        return 