# Pattern: Hash Map
# Time: O(n * k)
# Space: O(n)
# Idea: Use character frequency as key to group anagrams
# Trick: Convert count array into tuple so it can be a hashmap key

from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for s in strs:
            count = [0] * 26

            for c in s:
                # Convert character to integer
                val = ord(c) - ord('a')
                count[val] += 1

            # Use count as key to group anagrams
            key = tuple(count)
            res[key].append(s)
            
        return list(res.values())
