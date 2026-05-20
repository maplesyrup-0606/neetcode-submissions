class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        for point in points:
            x = point[0]
            y = point[1]
            heapq.heappush(heap, (-(x**2+y**2), [x, y]))
            while len(heap) > k:
                heapq.heappop(heap)
        
        ret = []
        for dist, coord in heap:
            ret.append(coord)
        
        return ret