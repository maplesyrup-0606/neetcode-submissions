class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(list)

        for num in nums:
            freq[num] += nums
        
        ret = []
        for key, val in freq.items():
            heapq.heappush(ret, (freq[key], key))
            if len(ret) > k:
                heapq.heappop(ret)
            
        res = []
        for smth in ret:
            res.append(smth[1])
        
        return res
