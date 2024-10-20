class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        minsum = triangle[-1]

        for i in range(len(triangle) - 2, -1, -1):
            for j in range(len(triangle[i])):
                minsum[j] = min(minsum[j], minsum[j+1]) + triangle[i][j]
        return minsum[0]