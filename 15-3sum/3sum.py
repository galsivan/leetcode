class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        a = 0
        while a < len(nums):
            l, r = a + 1, len(nums) - 1
            while l < r:
                total = nums[a] + nums[l] + nums[r]
                if total > 0:
                    r -= 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
                elif total < 0:
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                elif total == 0:
                    res.append([nums[a], nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
            a += 1
            while a < len(nums) and nums[a] == nums[a - 1]:
                a += 1
        return res

        