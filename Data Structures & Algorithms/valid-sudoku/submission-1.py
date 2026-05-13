class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        squares = [set() for _ in range(9)]
        valid = set("123456789")
        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num == "." : continue
                if num not in valid: return False
                
                row_set = rows[i]
                if num in row_set: return False
                row_set.add(num)
            
                col_set = cols[j]
                if num in col_set: return False
                col_set.add(num)

                box_set = squares[3 * (i // 3) + (j // 3)]
                if num in box_set: return False
                box_set.add(num)
        
        return True