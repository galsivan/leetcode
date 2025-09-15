class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_subarray = nums[0]
        cur_sum = 0
        for n in nums:
            if cur_sum < 0:
                cur_sum = 0
            cur_sum += n

            max_subarray = max(max_subarray, cur_sum)
        return max_subarray