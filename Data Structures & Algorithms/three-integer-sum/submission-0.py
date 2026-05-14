class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # first, sort the array
        # second, we can do a two sum approach
        # third, keep track of previous combinations by tuples
        nums.sort()
        n = len(nums)
        seen = set()
        ret = []
        for i in range(n):
            target = -nums[i]
            for j in range(i + 1, n):
                find = target - nums[j]
                l = j + 1
                r = n - 1

                while l <= r:
                    mid = l + (r - l) // 2
                    if nums[mid] == find:
                        comb = [nums[i], nums[j], nums[mid]]
                        comb.sort()
                        comb = tuple(comb)

                        if comb not in seen:
                            seen.add(comb)
                            ret.append(list(comb))
                        break

                    elif nums[mid] > find:
                        r = mid - 1
                    else:
                        l = mid + 1
            
        return ret