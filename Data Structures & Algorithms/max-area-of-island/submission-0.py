class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ret = 0
        n, m = len(grid), len(grid[0])
        directions = ((1,0),(0,1),(-1,0),(0,-1))

        def dfs(pos, visited, grid):
            i, j = pos
            if i < 0 or i >= n or j < 0 or j >= m:
                return 0
            
            if grid[i][j] == 0:
                return 0
            
            if pos in visited:
                return 0
            
            visited.add(pos)
            grid[i][j] = 0
            res = 1
            for direction in directions:
                new_i = i + direction[0]
                new_j = j + direction[1]
                res += dfs((new_i,new_j), visited, grid)
            
            return res
        set_ = set()
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    ret = max(ret, dfs((i, j), set_, grid))
                
        return ret