from bisect import bisect_left


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        subsequence = [nums[0]]

        for i in range(1, len(nums)):
            j = bisect_left(subsequence, nums[i])
            if j < len(subsequence):
                subsequence[j] = nums[i]
            else:
                subsequence.append(nums[i])
        return len(subsequence)