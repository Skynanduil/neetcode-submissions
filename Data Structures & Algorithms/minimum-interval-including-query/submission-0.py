class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        sorted_queries = sorted([(q, idx) for idx, q in enumerate(queries)])

        result = [-1] * len(queries)

        min_heap = []
        i = 0

        for q, original_idx in sorted_queries:
            while i < len(intervals) and intervals[i][0] <= q:
                length = intervals[i][1] - intervals[i][0] + 1
                end_time = intervals[i][1]
                heapq.heappush(min_heap, (length, end_time))
                i += 1
            
            while min_heap and min_heap[0][1] < q:
                heapq.heappop(min_heap)
            
            if min_heap:
                result[original_idx] = min_heap[0][0]
            
        return result