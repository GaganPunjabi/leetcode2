class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        prev_dp = [1] * (len(s) + 1)
        for i in range(len(t) - 1, -1, -1): # 2
            cur_dp = [0] * (len(s) + 1)
            for j in range(len(s) - 1, -1, -1): # 6
                if t[i] == s[j]:
                    cur_dp[j] = cur_dp[j+1] + prev_dp[j+1]
                else:
                    cur_dp[j] = cur_dp[j + 1]
            prev_dp = cur_dp
        return prev_dp[0]
