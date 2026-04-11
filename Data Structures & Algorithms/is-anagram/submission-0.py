# Pattern: Hash Map
# Time: 0(n)
# Space: 0(1)
# Idea: Increment for s, decrement for t -> All counts must be 0
# Trick: Use one hashmap instead of two
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_len: int = len(s)
        
        # Early exit if strings are of different lengths
        if s_len != len(t):
            return False
        
        count: dict[str, int] = {}

        for i in range(s_len):
            # If it exists in s, increment
            # If it exists in t, decrement
            count[s[i]] = count.get(s[i], 0) + 1
            count[t[i]] = count.get(t[i], 0) - 1
        
        # Expect all counts to be 0
        return all(v == 0 for v in count.values())
