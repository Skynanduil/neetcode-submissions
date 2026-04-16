class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()

        prev_end = intervals[0][1]
        removals = 0

        for i in range(1, len(intervals)):
            current = intervals[i]
            if current[0] < prev_end:
                removals += 1
                prev_end = min(prev_end, current[1])
            
            else:
                prev_end = current[1]

        return removals