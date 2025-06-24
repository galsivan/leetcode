class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        d = {}

        for i, num in enumerate(numbers):
            if (target - num) not in d:
                d[num] = i
            else:
                return [d[target - num] + 1, i + 1]