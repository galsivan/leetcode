class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {
            "{": "}",
            "[": "]",
            "(": ")"
        }

        for c in s:
            if c in pairs:
                stack.append(c)
            else:
                if len(stack) == 0 or pairs[stack.pop()] != c:
                    return False
        
        if len(stack) > 0:
            return False
        
        return True
        