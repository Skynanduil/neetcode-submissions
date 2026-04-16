class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals)
        result = [intervals[0]]

        for i in range(len(intervals)):
            current = intervals[i]
            last_added = result[-1]

            if current[0] <= last_added[1]:
                last_added[1] = max(last_added[1], current[1])
            else:
                result.append(current)
        return result