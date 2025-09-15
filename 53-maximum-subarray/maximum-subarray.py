class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_subarray = nums[0]
        l, r = 0, 1
        cur_sum = max_subarray
        while r < len(nums):
            if cur_sum < 0:
                cur_sum = 0
                l += r
            cur_sum += nums[r]

            max_subarray = max(max_subarray, cur_sum)
            r += 1
        return max_subarray