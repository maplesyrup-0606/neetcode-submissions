class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)

        freq = {}
        for i in range(n):
            find = target - nums[i]
        
            if find in freq:
                return [min(i, freq[find]), max(i, freq[find])]
            else:
                freq[nums[i]] = i