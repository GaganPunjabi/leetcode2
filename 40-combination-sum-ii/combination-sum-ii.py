class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def backtrack(cur, i, total):
            if total == target:
                res.append(cur.copy())
            elif total > target or i == len(candidates):
                return
            else:
                cur.append(candidates[i])
                backtrack(cur, i+1, total + candidates[i])
                cur.pop()
                
                while i + 1 < len(candidates) and candidates[i] == candidates[i+1]:
                    i+=1
                backtrack(cur, i+1, total)
        backtrack([], 0 ,0)
        return res
                