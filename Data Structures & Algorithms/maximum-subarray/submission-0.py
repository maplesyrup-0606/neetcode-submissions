class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
            largest running sum
        """

        runningSum = 0
        maxRunningSum = float('-inf')
        for num in nums:
            runningSum = max(runningSum + num, num)
            maxRunningSum = max(maxRunningSum, runningSum)
        
        return maxRunningSum