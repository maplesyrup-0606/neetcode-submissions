class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
            For each encounter of 1, add 1 to the total count and add zero
        """
        n, m = len(grid), len(grid[0])        
        directions = ((-1,0),(1,0),(0,-1),(0,1))
        def print_grid(grid):
            for i in range(n):
                st = ""
                for j in range(m):
                    st += grid[i][j] + " "
                print(st)
            print()
            return
        # print_grid(grid)


        def dfs(pos, visited, grid):
            i, j = pos
            if i >= n or i < 0 or j >= m or j < 0:
                return
            if pos in visited : return
            if grid[i][j] == '0': return
            
            grid[i][j] = '0'
            visited.add((i,j))
            for direction in directions:
                new_i = i + direction[0]
                new_j = j + direction[1]

                dfs((new_i, new_j), visited, grid)
            
        count = 0
        visited = set()
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1':
                    count += 1
                    dfs((i,j), visited, grid)

                # print_grid(grid)
        
        return count