class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        longest = 0
        for num in s:
            if num - 1 not in s:
                count = 1
                while num + count in s:
                    count += 1
                longest = count if count > longest else longest
        return longest