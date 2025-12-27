class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True

        """ Case 1: If string is empty and first pattern is *
            Case 2: If string matches or ?, then prev result
            Case 3: If *, then result of prev char in string or prev pattern
        """
        # Step 1: Truncate multiple '*' to single '*'
        new_p = ""
        for char in p:
            if not (new_p and new_p[-1] == '*' and char == '*'):
                new_p += char
        p = new_p
        n = len(p)

        if n > 0:
            dp[0][1] = p[0] == '*'
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == '*':
                    include = dp[i - 1][j]
                    exclude = dp[i][j - 1]
                    dp[i][j] = include or exclude
                else:
                    
                    dp[i][j] = dp[i - 1][j - 1] and (s[i - 1] == p[j - 1] or p[j - 1] == '?')
        return dp[m][n]