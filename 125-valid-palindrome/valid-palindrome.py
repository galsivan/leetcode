class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = []
        for c in s:
            if (ord(c) <= ord('z') and ord(c) >= ord('a')) or \
                (ord(c) <= ord('Z') and ord(c) >= ord('A')) or \
                (ord(c) <= ord('9') and ord(c) >= ord('0')):
                new_s.append(c)

        s = "".join(new_s).lower()

        if len(s) == 0:
            return True

        l, r = 0, len(s) - 1

        while l <= r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        
        return True
        