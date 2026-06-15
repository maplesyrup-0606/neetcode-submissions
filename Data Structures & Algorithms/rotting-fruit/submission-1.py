class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        oranges = deque([])
        n, m = len(grid), len(grid[0])
        fresh = 0
        visited = set()
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    oranges.append((i, j))
                    visited.add((i, j))
                elif grid[i][j] == 1:
                    fresh += 1
        
        if fresh == 0: return 0

        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
        time = 0

        while oranges:
            p = len(oranges)
            for i in range(p):
                x, y = oranges.popleft()
                visited.add((x, y))

                for dx, dy in directions: 
                    x2 = x + dx
                    y2 = y + dy

                    if x2 < 0 or x2 >= n or y2 < 0 or y2 >= m:
                        continue
                    if (x2, y2) in visited:
                        continue

                    if grid[x2][y2] == 1:
                        fresh -= 1
                        oranges.append((x2, y2))
                        grid[x2][y2] = 2
                    
            time += 1

        return time - 1 if (fresh == 0) else -1 