class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        """
            For each number we have two possible operations 
                1. add
                2. subtract

            First approach is back track
        """
        n = len(nums)
        def dfs(idx, prevSum, positive):
            currSum = prevSum + nums[idx] if positive else prevSum - nums[idx]
            if idx == n - 1:
                if currSum == target:
                    return 1
                
                else:
                    return 0
                
        
            return dfs(idx + 1, currSum, True) + dfs(idx + 1, currSum, False)
        
        return dfs(0, 0, True) + dfs(0, 0, False)