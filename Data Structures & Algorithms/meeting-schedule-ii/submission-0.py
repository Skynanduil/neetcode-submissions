"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        starts = sorted([i.start for i in intervals])
        ends = sorted([i.end for i in intervals])

        rooms = 0
        end_i = 0

        for start in starts:
            if start < ends[end_i]:
                rooms += 1
            else: 
                end_i += 1
        
        return rooms