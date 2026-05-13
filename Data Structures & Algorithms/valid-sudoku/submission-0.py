class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        valid = set("123456789")
        n, m = 9, 9
        # row major
        for i in range(9):
            currrow = board[i]
            seen = set()
            for num in currrow:
                if num == "." : continue
                if num not in valid:
                    return False
                
                if num in seen:
                    return False
                
                seen.add(num)
        
        # col order
        for j in range(9):
            seen = set()
            for i in range(9):
                num = board[i][j]

                if num == ".": continue
                if num not in valid: return False
                if num in seen: return False
            
                seen.add(num)
            
        
        # squares
        for i in range(3):
            i_idx = 3 * i
            for j in range(3):
                j_idx = 3 * j
                seen = set()
                for new_i in range(i_idx, i_idx + 3):
                    for new_j in range(j_idx, j_idx + 3):
                        num = board[new_i][new_j]

                        if num == ".": continue
                        if num not in valid: return False
                        if num in seen: return False
                    
                        seen.add(num)
        return True