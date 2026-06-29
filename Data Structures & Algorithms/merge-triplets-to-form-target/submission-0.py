class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        
        ret = [float('-inf'), float('-inf'), float('-inf')]
        tx, ty, tz = target
        for x, y, z in triplets:
            if x > tx or y > ty or z > tz:
                continue
            
            ret[0] = max(ret[0], x)
            ret[1] = max(ret[1], y)
            ret[2] = max(ret[2], z)

        return ret == target