class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        mid = sum(stones) // 2
        dp = {0,}

        for i in range(len(stones)):
            cur_dp = dp.copy()
            for wt in dp:
                if wt + stones[i] <= mid:
                    cur_dp.add(wt + stones[i])
            dp = cur_dp
        return sum(stones) - max(dp) * 2
                
