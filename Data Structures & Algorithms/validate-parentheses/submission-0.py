class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        opening_brackets = set(brackets.values())

        for c in s:
            if c in brackets:
                if not stack:
                    return False

                o = stack.pop()
                if brackets[c] != o:
                    return False
            elif c in opening_brackets:
                stack.append(c)
            else:
                continue
        return not stack
