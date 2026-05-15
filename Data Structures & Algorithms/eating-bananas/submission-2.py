class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def eating_time(rate, bananas):
            time = 0
            for banana in bananas:
                time += math.ceil(banana / rate)
            
            return time

        l, r = 1, max(piles)
        ret = r
        while l <= r:
            mid = l + (r - l) // 2
            time = eating_time(mid, piles)
            if time <= h:
                r = mid - 1
                ret = min(ret, mid)
            else:
                l = mid + 1
        
        return ret
