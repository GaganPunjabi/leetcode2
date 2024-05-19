class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        output = []

        for i in range(2**n, 2 ** (n + 1)):
            bitmask = bin(i)[3:]
            output.append([nums[j] for j in range(n) if bitmask[j] == "1"])
        return output
    
# 1000, 1001, 1010, 1011, 1100, 1101, 1110, 1111