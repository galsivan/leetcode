class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        # pick smallest x pair and highest x pair o(n)
        pair1 = min(coordinates, key=lambda x: x[0])
        pair2 = max(coordinates, key=lambda x: x[0])

        # calc m and b in y = mx + b
        if pair2[0] == pair1[0]:
            prev = coordinates[0][0]
            for i in range(1, len(coordinates)):
                if prev != coordinates[i][0]:
                    return False
                prev = coordinates[i][0]
            return True

        m = (pair2[1] - pair1[1]) / (pair2[0] - pair1[0])
        b = pair1[1] - m*pair1[0]

        for pair in coordinates:
            if pair[1] != m * pair[0] + b:
                return False
        return True

        