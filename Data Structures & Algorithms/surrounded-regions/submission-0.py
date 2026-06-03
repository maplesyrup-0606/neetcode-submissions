class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
            for each O, we can BFS, if we can hit boundaries we're fine otherwise change to X
        """

        n, m = len(board), len(board[0])
        directions = ((1,0), (0,1), (-1,0), (0, -1))

        def bfs(origin):
            level = deque([origin])
            visited = set()
            while level:
                # print(origin, level, visited)
                num = len(level)
                for i in range(num):
                    x, y = level.popleft()

                    if board[x][y] == 'X':
                        continue

                    if x == 0 or x == n - 1 or y == 0 or y == m - 1:
                        return
                    
                    if (x, y) in visited:
                        continue
                    
                    visited.add((x, y))

                    for direction in directions:
                        new_x = x + direction[0]
                        new_y = y + direction[1]
                        level.append((new_x, new_y))
            return visited

        for i in range(n):
            for j in range(m):
                if board[i][j] == 'O' and (i != 0 or i != n - 1 or j != 0 or j != m - 1):
                    res = bfs((i, j))
                    if res:
                        for x, y in res:
                            board[x][y] = 'X'