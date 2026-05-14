class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # amount of trapped water = width * min(height_l, height_r)
        # do a two pointer approach
        # move inwards on direction that has higher 
        l, r = 0, len(heights) - 1
        ret = 0
    
        while l < r:
            # print(l, r)
            curr_height = min(heights[l], heights[r])
            water = (r - l) * curr_height
            ret = max(ret, water)
        
            if heights[l] < heights[r]:
                l += 1
            else :
                r -= 1
        return ret