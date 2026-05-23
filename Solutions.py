# Problem: Regular Expression Matching
# Difficulty: Hard
# Link: https://leetcode.com/problems/regular-expression-matching/
# Approach: Dynamic Programming
# Time Complexity: O(m x n)
# Space Complexity: O(m x n)

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True

        for j in range(2, n + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 2]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == '*':
                    zero_occurrence = dp[i][j - 2]
                    preceding_matches = p[j - 2] in {s[i - 1], '.'}
                    one_or_more = preceding_matches and dp[i - 1][j]
                    dp[i][j] = zero_occurrence or one_or_more
                elif p[j - 1] == '.' or p[j - 1] == s[i - 1]:
                    dp[i][j] = dp[i - 1][j - 1]

        return dp[m][n]
