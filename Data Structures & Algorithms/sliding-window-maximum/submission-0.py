class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ret = []

        for i in range(len(nums) - k + 1):
            ret.append(max(nums[i : i + k]))
        return ret