class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp = [[0 for _ in range(n)] for _ in range(n)]
        count = 0

        for i in range(n):
            dp[i][i] = 1
            count += 1

        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                if s[i] == s[j]:
                    if length == 2 or dp[i + 1][j - 1] == length - 2:
                        dp[i][j] = length
                        count += 1

        return count
