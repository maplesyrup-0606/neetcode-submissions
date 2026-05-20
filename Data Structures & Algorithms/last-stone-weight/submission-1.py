class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []

        for stone in stones:
            heapq.heappush(heap, -stone)
        
        while len(heap) >= 2:
            heaviest = heapq.heappop(heap)
            nextHeaviest = heapq.heappop(heap)
            if heaviest == nextHeaviest:
                continue
            else:
                rest = heaviest - nextHeaviest
                heapq.heappush(heap, rest)
    
        return -heap[0] if heap else 0