class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        output = []

        for i in range(len(intervals)):
            if intervals[i][1] < newInterval[0]:
                output.append(intervals[i])
            elif intervals[i][0] > newInterval[1]:
                output.append(newInterval)
                return output + intervals[i:]
            else:
                newInterval[0] = min(newInterval[0], intervals[i][0])
                newInterval[1] = max(newInterval[1], intervals[i][1])
            
        output.append(newInterval)
        return output