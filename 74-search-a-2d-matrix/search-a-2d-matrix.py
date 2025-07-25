class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        l, r = 0, m * n - 1

        while l <= r:
            i = (l + r) // 2

            if matrix[i // n][i % n] == target:
                return True
            
            if matrix[i // n][i % n] < target:
                l = i + 1
            else:
                r = i - 1

        return False