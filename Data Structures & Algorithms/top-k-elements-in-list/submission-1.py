class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)

        for num in nums:
            freq[num] += 1
        
        # now make a length k list and keep track in smallest order
        # or we just sort it
    
        freq = {key : val for key, val in sorted(freq.items(), key=lambda item: item[1], reverse=True)}
        
        ret = []
        i = 0
        for key, val in freq.items():
            if i >= k:
                break
            ret.append(key)
            i += 1
        
        return ret