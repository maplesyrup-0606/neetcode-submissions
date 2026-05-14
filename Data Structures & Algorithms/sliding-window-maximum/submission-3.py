class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """
        for each window, we have one incoming, and one outgoing
        if the incoming is higher than the max then we're fine
        also if both incoming and outgoing are smaller than the max we're fine
        however, if the outgoing is the max then we need to update
        """
        if k >= len(nums): return [max(nums)]
        if k == 1: return nums

        sub = nums[0 : k]
        curr_max = max(sub)
        ret = [curr_max]

        for i in range(1, len(nums) - k + 1):
            outgoing = nums[i - 1]
            incoming = nums[i + k - 1]
            
            if incoming > curr_max:
                curr_max = incoming
            
            elif incoming < curr_max and outgoing < curr_max:
                pass
            
            elif outgoing == curr_max and incoming < curr_max:
                # need to update the maximum now to something else
                curr_max = max(nums[i : i + k])
            
            ret.append(curr_max)
        
        return ret