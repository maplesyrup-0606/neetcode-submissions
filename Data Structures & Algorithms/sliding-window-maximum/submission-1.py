class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if k == len(nums): return [max(nums)]
        n = len(nums)
        sub = nums[0 : k]
        curr_max = max(sub)
        ret = [curr_max]

        for i in range(1, n - k + 1):
            """
            case 1: outgoing is the maximum -> find new max
            case 2: incoming is the new maximum -> update maximum
            case 3: neither are maximum -> nothing
            """
            outgoing = nums[i - 1]
            incoming = nums[i + k - 1]
            
            if outgoing == curr_max:
                curr_max = max(nums[i : i + k])
            elif incoming > curr_max:
                curr_max = incoming
            
            ret.append(curr_max)


        return ret