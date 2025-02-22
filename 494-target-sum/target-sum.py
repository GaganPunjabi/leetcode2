from collections import defaultdict


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        prev_dp = defaultdict(int)
        prev_dp[0] = 1
        for i in range(len(nums)):
            cur_dp = defaultdict(int)
            for j, count in prev_dp.items():
                cur_dp[j - nums[i]] += count
                cur_dp[j + nums[i]] += count
            prev_dp = cur_dp
        return prev_dp[target]
