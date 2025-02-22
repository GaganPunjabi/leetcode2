class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        prev_dp = [0] * (2*sum(nums) + 1)
        prev_dp[sum(nums)] = 1
        if -sum(nums) > target or sum(nums) < target:
            return 0
        for i in range(len(nums)):
            cur_dp = [0] * (2*sum(nums) + 1)
            for j in range(len(cur_dp)):
                if j - nums[i] >= 0:
                    cur_dp[j] += prev_dp[j - nums[i]]
                if j + nums[i] < (2*sum(nums) + 1):
                    cur_dp[j] += prev_dp[j + nums[i]]
            prev_dp = cur_dp
            print(prev_dp)
        return prev_dp[sum(nums) + target]
