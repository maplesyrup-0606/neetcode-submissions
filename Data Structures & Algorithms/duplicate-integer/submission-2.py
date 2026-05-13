class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        res = {}
        for idx, num in enumerate(nums):
            if num in res:
                return True
            else:
                res[num] = idx
    
        return False