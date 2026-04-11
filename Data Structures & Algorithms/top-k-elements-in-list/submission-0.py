# Pattern: Hash Map + Bucket Sort
# Time: O(n)
# Space: O(n)
# Idea: Group numbers by frequency, iterate from highest frequency
# Trick: Use index as frequency

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Count frequency
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1

        # Create buckets where the index is the frequency
        freq = [[] for _ in range(len(nums) + 1)]
        for num, c in count.items():
            freq[c].append(num)

        # Collect top k
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res
