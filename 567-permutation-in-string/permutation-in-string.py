class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l, r = 0, len(s1) - 1
        s1_count = {}
        s2_count = {}

        for c in s1:
            s1_count[c] = 1 + s1_count.get(c, 0)
        for c in s2[l:r+1]:
            s2_count[c] = 1 + s2_count.get(c, 0)
        if s1_count == s2_count:
                return True

        while r < len(s2) - 1:
            r += 1
            s2_count[s2[r]] = 1 + s2_count.get(s2[r], 0)
            s2_count[s2[l]] -= 1
            if s2_count[s2[l]] == 0:
                del(s2_count[s2[l]])
            l += 1
            if s1_count == s2_count:
                return True
        return False
        