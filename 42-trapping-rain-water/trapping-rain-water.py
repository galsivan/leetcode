class Solution:
    def trap(self, height: List[int]) -> int:
        prefix = [0] * len(height)
        suffix = [0] * len(height)
        res = 0
        for i in range(1, len(height)):
            prefix[i] = max(prefix[i-1], height[i-1])
            suffix[len(height) - i -1] = max(suffix[len(height) - i], height[len(height) - i])

        print(prefix)
        print(suffix)
        
        for i in range(len(height)):
            res += max(0, min(prefix[i], suffix[i]) - height[i])
        return res