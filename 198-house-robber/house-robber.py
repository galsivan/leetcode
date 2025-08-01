class Solution:
    def rob(self, nums: List[int]) -> int:
        # def dfs(i):
        #     if i == 0:
        #         return nums[0]
        #     if i == 1:
        #         return max(nums[0], nums[1])
        #     return max(nums[i] + dfs(i - 2), dfs(i - 1))
        # return dfs(len(nums) - 1)

        res = [0] * len(nums)
        res[0] = nums[0]
        if len(res) > 1:
            res[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            res[i] = max(nums[i] + res[i - 2], res[i - 1])
        
        return res[-1]



