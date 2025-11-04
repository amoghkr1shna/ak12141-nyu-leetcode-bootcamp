class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        MOD = 10**9 + 7
        share = 0
        dp = [0] * n
        dp[0] = 1

        for i in range(1, n):
            if i - delay >= 0:
                share = (share + dp[i - delay]) % MOD
                # people who learned delay days ago being sharing today
            if i - forget >= 0:
                share = (share - dp[i - forget]) % MOD
                #people who learned forget days ago forget today
            dp[i] = share % MOD

        res = 0
        for i in range(n - forget, n):
            if i >= 0:
                res = (res + dp[i]) % MOD

        return res
