# Pattern: String parsing
# Time: O(n)
# Space: O(n)
# Idea: Prefix each string with its length and a delimiter
# Trick: Read exact number of characters after the delimiter
class Solution:
    delim: str = "#"

    def encode(self, strs: List[str]) -> str:
        res: str = ""
        # Parse string using the length of the word and a delimiter
        for s in strs:
            res += f"{len(s)}{self.delim}{s}"
        return res

    def decode(self, s: str) -> List[str]:
        res: List[str] = []
        i = 0
        
        while i < len(s):
            j = i
            while s[j] != self.delim:
                j += 1
            
            length = int(s[i:j])
            word = s[j + 1: j + 1 + length]
            res.append(word)

            i = j + 1 + length
        return res
