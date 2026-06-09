class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        """
            residue at each point
            gas[i] - cost[i]
        """
        ret = -1

        n = len(gas)
        for i in range(n):
            start = i
            residual = gas[i] - cost[i]

            if residual >= 0:
                j = (i + 1) % n
                while True:
                    if j == start:
                        return start 
                    
                    residual += gas[j] - cost[j]
                    if residual < 0:
                        break
                    
                    j = (j + 1) % n
        return -1