class Solution:
    def canJump(self, nums: List[int]) -> bool:
 
        n = len(nums)
        if n == 1: return True
        ret = [False for _ in range(n)]
        ret[0] = True
        for idx, jump in enumerate(nums):
            if ret[idx]:
                for i in range(1,jump+1):
                    if idx + i < n:
                        ret[idx + i] = True
        
        return ret[-1]