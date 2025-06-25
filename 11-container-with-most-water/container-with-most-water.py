class Solution:
    def maxArea(self, height: List[int]) -> int:
        l,r = 0, len(height) - 1
        area = 0

        while l < r:
            if height[l] <= height[r]:
                area = max(area, (r - l) * height[l])
                l += 1
            else:
                area = max(area, (r - l) * height[r])
                r -= 1
        return area
