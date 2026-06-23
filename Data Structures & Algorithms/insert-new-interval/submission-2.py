class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # find last insert-able point

        n = len(intervals)
        if n == 0: return [newInterval]

        lastStart, lastEnd = intervals[-1]
        newStart, newEnd = newInterval

        #    return intervals + [newInterval]
        

        # 1. Using the start of the new one figure where it belongs
        i = 0
        while i < n:
            currStart, currEnd = intervals[i]
        
            if newStart < currStart:
                break

            i += 1

        if i == n - 1:
            if lastStart > intervals[i][0]:
                intervals.append(newInterval)
            else:
                intervals.insert(i, newInterval)
                n += 1
        else:
            intervals.insert(i, newInterval)
            n += 1
        res = []

        j = 0
        while j < n:
            currStart, currEnd = intervals[j]
            updatedEnd = currEnd
            
            k = j + 1
            while k < n:
                newStart, newEnd = intervals[k]
                if newStart > updatedEnd:
                    break
                
                updatedEnd = max(updatedEnd, newEnd)
                k += 1
            res.append([currStart, updatedEnd])
            j = k
        
        return res