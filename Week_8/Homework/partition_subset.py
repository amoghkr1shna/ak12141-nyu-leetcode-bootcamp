class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums) #getting total of all elements
        if total % 2 != 0: #if the total's odd, then we can't halve it
            return False

        tgt = total // 2 #since they're halved, we'd theoretically need half of the total sum
        dp = [False] * (tgt + 1) #store whether we can make the target sum
        dp[0] = True #base case

        for n in nums:
            for i in range(tgt, n - 1, -1): #iterating backwards to make sure we're not reusing elements
                dp[i] = dp[i] or dp[i - n] #either we can make the target with the current num, or without it

        return dp[tgt]