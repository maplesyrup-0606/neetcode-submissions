class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        i = 0
        intervals.sort(key=lambda x: x[0])
        
        # print(intervals)
        while i < len(intervals) - 1:
            currStart, currEnd = intervals[i]
            nextStart, nextEnd = intervals[i + 1]
            if currStart <= nextStart and nextStart <= currEnd:
                intervals.pop(i)
                intervals[i][0] = min(currStart, nextStart)
                intervals[i][1] = max(currEnd, nextEnd)
                i -= 1
            i += 1
            # print(intervals)
        return list(intervals)