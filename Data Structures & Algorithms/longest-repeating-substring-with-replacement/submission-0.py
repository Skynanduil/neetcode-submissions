from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = defaultdict(int)
        max_freq = 0
        left = 0
        max_length = 0

        for right in range(len(s)):
            count[s[right]] += 1

            max_freq = max(max_freq, count[s[right]])

            if (right - left + 1) - max_freq > k:
                count[s[left]] -= 1
                left += 1
        
            max_length = max(max_length, right - left + 1)
        
        return max_length