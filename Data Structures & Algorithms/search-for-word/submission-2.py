class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        """
            For a starting character, we can traverse in all directions.
            For each instance, we need to keep a track of the visited nodes.
        """
        directions = ((0,1),(0,-1),(1,0),(-1,0))
        n = len(board)
        m = len(board[0])
        def dfs(index, visited, constructed):
            if constructed == word:
                return True
            if index in visited:
                return False

            if len(constructed) > len(word):
                return False

            visited.add(index)
            x = index[0]
            y = index[1]

            if x >= n or y >= m or x < 0 or y < 0:
                return False

            res = False 
            for direction in directions:
                new_x = x + direction[0]
                new_y = y + direction[1]
                res = res or dfs((new_x, new_y), visited.copy(), constructed + board[x][y])

            return res

        start = word[0]

        for i in range(n):
            for j in range(m):
                if board[i][j] == start:
                    res = dfs((i, j), set([]), "")
                    if res: return True
                else:
                    continue
        
        return False