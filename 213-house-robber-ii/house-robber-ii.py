class Solution:
    def rob(self, nums: List[int]) -> int:        
        if len(nums) == 1:
            return nums[0]

        if len(nums) == 2:
            return max(nums[0], nums[1])

        prev = nums[0]
        curr = max(nums[0], nums[1])

        cir_prev = nums[1]
        cir_curr = max(nums[1], nums[2])

        for i in range(2, len(nums) - 1):
            print(i)
            print(curr)
            prev, curr = curr, max(nums[i] + prev, curr)

        for i in range(3, len(nums)):
            cir_prev, cir_curr = cir_curr, max(nums[i] + cir_prev, cir_curr)
        
        print(curr, cir_curr)
        return max(curr, cir_curr)

    #     if len(nums) == 0 or nums is None:
    #         return 0

    #     if len(nums) == 1:
    #         return nums[0]

    #     return max(self.rob_simple(nums[:-1]), self.rob_simple(nums[1:]))

    # def rob_simple(self, nums: List[int]) -> int:
    #     t1 = 0
    #     t2 = 0
    #     for current in nums:
    #         temp = t1
    #         t1 = max(current + t2, t1)
    #         t2 = temp

    #     return t1

        