class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(cost)
        """
            we want to find the starting index where we never reach a running sum of negative EVER
        """
        runningRes = 0
        start = 0

        for i in range(2*n):
            runningRes += gas[i % n] - cost[i % n]
            if runningRes < 0:
                start = i + 1
                runningRes = 0
        
        if start >= n or runningRes < 0:
            return -1
        
        return start