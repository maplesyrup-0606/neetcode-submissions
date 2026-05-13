class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left_prod = []
        left = 1
        for num in nums:
            left_prod.append(left)
            left *= num

        right_prod = [0 for _ in range(n)]
        right = 1
        for i in range(n - 1, - 1, - 1):
            right_prod[i] = right
            right *= nums[i]
        
        res = [0 for _ in range(n)]
        for i in range(n):
            res[i] = left_prod[i] * right_prod[i]
        
        return res
