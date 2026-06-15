class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        visited = set()
        n, m = len(matrix), len(matrix[0])

        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    if (i, j) in visited:
                        continue
                    else:
                        for k in range(n):
                            if matrix[k][j] == 0:
                                continue
                            matrix[k][j] = 0
                            visited.add((k, j))
                        for l in range(m):
                            if matrix[i][l] == 0:
                                continue
                            matrix[i][l] = 0
                            visited.add((i, l))
                    