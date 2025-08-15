class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3) or  (not s1 and s2 != s3) or  (not s2 and  s1 != s3) :
            return False
        

        prev_dp = [False] * (len(s2) + 1)
        prev_dp[-1] = True

        for i in range(len(s1), -1, -1):
            cur_dp = [False]* (len(s2) + 1)
            cur_dp[-1] = True
            for j in range(len(s2), -1, -1):
                if i < len(s1) and prev_dp[j] and s1[i] == s3[i+j]:
                    cur_dp[j] = True
                elif j < len(s2) and cur_dp[j+1] and s2[j] == s3[i+j]:
                    cur_dp[j] = True
            prev_dp = cur_dp
        return prev_dp[0]

 