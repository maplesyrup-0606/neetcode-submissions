class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ret = deque([[]])

        """
        For each element we have the option of including or not including
        """

        for num in nums:
            n = len(ret)
            for i in range(n):
                node = ret.popleft()
                ret.append(node)
                ret.append(node + [num])
            
            print(ret)
    
        return list(ret)