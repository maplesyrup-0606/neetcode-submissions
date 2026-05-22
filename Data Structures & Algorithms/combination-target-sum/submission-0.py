class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        self.ret = []
        recorded = set()

        def backtrack(nums, idx, sub, sum):
            if idx >= len(nums):
                return
            if sum > target:
                return
            if sum == target:
                if tuple(sub) in recorded:
                    return
                
                recorded.add(tuple(sub))
                
                self.ret.append(sub)
            backtrack(nums, idx, sub + [nums[idx]], sum + nums[idx])
            backtrack(nums, idx + 1, sub, sum)

        for idx, num in enumerate(nums):
            backtrack(nums, idx, [num], num)
        
        return self.ret