class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        either rob 1st or last and do the same thing
        """
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums)
        
        dp = [0 for _ in range(n)]
        dp[0] = nums[0]
        # exclude last 
        for i in range(1, n - 1):
            dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])

        # exclude first
        dp2 = [0 for _ in range(n)]
        dp2[0] = 0
        for i in range(1, n):
            dp2[i] = max(dp2[i - 2] + nums[i], dp2[i - 1])
        
        return max(dp[-2],dp2[-1])