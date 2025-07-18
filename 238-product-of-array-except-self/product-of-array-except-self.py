class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l, r = 1, len(nums) - 2
        prefix = [1] * len(nums)
        suffix = [1] * len(nums)
        res = []
        while l < len(nums):
            prefix[l] = nums[l - 1] * prefix[l - 1]
            suffix[r] = nums[r + 1] * suffix[r + 1]
            l += 1
            r -= 1
        i = 0
        while i < len(nums):
            res.append(prefix[i] * suffix[i])
            i += 1
        return res




        