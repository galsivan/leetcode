class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])


        def inner_rob(inner):
            prev = inner[0]
            curr = max(inner[0], inner[1])

            for i in range(2, len(inner)):
                prev, curr = curr, max(inner[i] + prev, curr)
            
            return curr
        
        return max(inner_rob(nums[:-1]), inner_rob(nums[1:]))