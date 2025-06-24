class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        l = 0
        longest = 1
        maxF = 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            maxF = max(maxF, count[s[r]])
            if r - l + 1 - maxF <= k:
                longest = max(longest, r - l + 1)
                r += 1
            else:
                count[s[l]] -= 1
                l += 1
        return longest