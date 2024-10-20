class Solution:
    @staticmethod
    def bisect_left(a, x):
        lo, hi = 0, len(a)
        while lo < hi:
            mid = (lo+hi)//2
            if a[mid] < x: lo = mid+1
            else: hi = mid
        return lo

    def lengthOfLIS(self, nums: List[int]) -> int:
        subsequence = [nums[0]]

        for i in range(1, len(nums)):
            j = self.bisect_left(subsequence, nums[i])
            if j < len(subsequence):
                subsequence[j] = nums[i]
            else:
                subsequence.append(nums[i])
        return len(subsequence)