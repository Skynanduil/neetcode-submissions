from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        dict_t = Counter(t)
        required_unique = len(dict_t)

        window_counts = {}
        have = 0
        ans = (float("inf"), None, None)
        left = 0

        for right in range(len(s)):
            char = s[right]
            window_counts[char] = window_counts.get(char, 0) + 1

            if char in dict_t and window_counts[char] == dict_t[char]:
                have += 1
            
            while have == required_unique:
                if (right - left + 1) < ans[0]:
                    ans = (right - left + 1, left, right)
                
                left_char = s[left]
                window_counts[left_char] -= 1

                if left_char in dict_t and window_counts[left_char] < dict_t[left_char]:
                    have -= 1
                
                left += 1
        
        length, l, r = ans
        return s[l : r + 1] if length != float("inf") else ""