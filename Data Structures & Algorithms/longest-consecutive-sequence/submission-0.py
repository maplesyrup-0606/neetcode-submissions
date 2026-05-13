class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        move = defaultdict(int)
    
        for num in nums:
            if num not in move:
                move[num] = float('inf')
                if num - 1 in nums:
                    move[num - 1] = num
                if num + 1 in nums:
                    move[num] = num + 1
        
        ret = 0
        for k, v in move.items():
            val = k
            length = 0
            while val != float('inf'):
                val = move[val]
                length += 1
            
            ret = max(ret, length)
    
        return ret