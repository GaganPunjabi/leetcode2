class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        def countPallindrome(lp, rp):
            count = 0
            while lp >= 0 and rp < len(s) and s[lp] == s[rp]:
                lp -= 1
                rp += 1
                count += 1
            return count
        
        for i in range(len(s)):
            count += countPallindrome(i, i + 1) + countPallindrome(i, i)
        return count
