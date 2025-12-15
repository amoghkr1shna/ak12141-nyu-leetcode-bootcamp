class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # init variables using the first element.
        current = nums[0]
        maks = nums[0]

        # Starting with the 2nd element since we used the first one during initialization
        for n in nums[1:]:
            # If current's negative, discard
            # Else, keep adding to it.
            current = max(n, current + n)
            maks = max(maks, current)

        return maks