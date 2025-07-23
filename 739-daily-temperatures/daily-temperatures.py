class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []

        for i, temp in enumerate(temperatures):
            if not stack:
                stack.append(i)
                continue
            
            if temp < temperatures[stack[-1]]:
                stack.append(i)
            else:
                while stack and temp > temperatures[stack[-1]]:
                    res[stack[-1]] = i - stack[-1]
                    stack.pop()
                stack.append(i)
        
        return res