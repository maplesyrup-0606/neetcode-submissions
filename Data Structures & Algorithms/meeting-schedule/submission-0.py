"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals = sorted(intervals, key= lambda item: item.start)
        
        # we only need to compare next start and curr end

        for i in range(len(intervals) - 1):
            currInterval, nextInterval = intervals[i], intervals[i + 1]

            currStart, currEnd = currInterval.start, currInterval.end
            nextStart, nextEnd = nextInterval.start, nextInterval.end

            if currEnd > nextStart:
                return False

            
        return True