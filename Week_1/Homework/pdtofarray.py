# from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [1] * n
        #as per the hint on LeetCode, we can use an output array instead of using extra space
        #for this problem, we're doing 2 passes, left and right
        

        left = 1
        for i in range(n):
            # print(i)
            ans[i] = left
            left *=nums[i]
        # print(ans)
        # for the left pass, we multiply the values to the left of the current index
        # since there's nothing to the left of index 0, left's initialized as 1
        # for the example of [1,2,3,4], the left pass gives:
        # left of 1 = 1 (or nothing basically)
        # left of 2 = 1 (since 1's the only value to the left)
        # left of 3 = 1*2 = 2 (1,2,3)
        # left of 4 = 1*2*3 = 6 (1,2,3,4)
        # therefore the left pass gives us [1,1,2,6]


        right = 1
        for i in range(n-1,-1,-1):
            #we do n-1 since we're starting from the end
            # -1 for the steps, and we also use -1 as the end index since the end range isn't inclusive
            ans[i] *= right
            right *= nums[i]
            # same logic kind of applies
            # right of 4 = 1 (or nothing basically)
            #right of 3 = 4 so ans gets updated to 8
            # right of 2 = 3*4 = 12 so ans gets updated to 12*1 = 12
            # right of 1 = 2*3*4 = 24 so ans gets updated to 24*1 = 24

        return ans


#I initially thought of using one pointer and one pass and sliding window
# this doesnt work since we need to multiply all values except the current index
# and to reset the window, we'd need to divide or use modulo which isn't allowed