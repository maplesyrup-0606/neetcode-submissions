class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        l, r = 0, m * n - 1

        while l <= r:
            mid = l + (r - l) // 2
        
            mid_x = mid // n
            mid_y = mid % n
            mid_num = matrix[mid_x][mid_y]
        
            if mid_num == target:
                return True

            if mid_num > target:
                r = mid - 1
            else :
                l = mid + 1
    
        return False