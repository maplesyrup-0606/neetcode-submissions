"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals = sorted(intervals, key = lambda item: item.start)
        rooms = []

        # upon conflict, we choose the interval with min end point

        for interval in intervals:
            madeIn = False
            matchIngInterval = [float('inf'), float('inf'), -1]

            for idx, room in enumerate(rooms):
                roomStart, roomEnd = room[0], room[1]
                intStart, intEnd = interval.start, interval.end

                if roomEnd <= intStart:
                    if roomEnd < matchIngInterval[0]:
                        matchIngInterval = [roomStart, roomEnd, idx]
                        madeIn = True
            print(madeIn, matchIngInterval)
            if not madeIn:
                rooms.append([interval.start, interval.end])
            
            else:
                matchStart, matchEnd, matchIdx = matchIngInterval
                rooms[matchIdx][1] = interval.end 
        
        #smth = ""
        #for interval in intervals:
        #    smth += f"{(interval.start, interval.end)}" + " "
        #print(smth)
        #print(rooms)
        return len(rooms)