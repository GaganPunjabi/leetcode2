class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        subsequence = [nums[0]]

        for i in range(1, len(nums)):
            j = 0
            while j < len(subsequence) and subsequence[j] < nums[i]:
                j += 1
            if j < len(subsequence):
                subsequence[j] = nums[i]
            else:
                subsequence.append(nums[i])

        return len(subsequence)