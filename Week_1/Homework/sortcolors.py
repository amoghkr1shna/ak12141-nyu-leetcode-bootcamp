class Solution:
    def sortColors(self, nums: List[int]) -> None:
        low = 0
        mid = 0
        high = len(nums) - 1
        # three pointers since there are 3 colors or demarcations
        #like binary search, mid is the pointer that goes through the array

        while mid <=high:
            if nums[mid] == 0:
                nums[low] = nums[low] + nums[mid]
                nums[mid] = nums[low] - nums[mid]
                nums[low] = nums[low] - nums[mid]
                #swapping logic
                # a = a+b
                # b = a-b
                # a = a-b
                # we're swapping mid and low because we want 0s to be at the lower end of the array, which is to the left of mid
                low = low+1
                mid = mid+1
            elif nums[mid] == 1:
                mid = mid+1
                #doing this basically to skip the 1 and keep it in place and move to the next index
            elif nums[mid] == 2:
                nums[high] = nums[high] + nums[mid]
                nums[mid] = nums[high] - nums[mid]
                nums[high] = nums[high] - nums[mid]
                #swapping logic
                # we're swapping mid and high because we want 2s to be at the higher end of the array, which is to the right of mid

                high = high-1
                # we only update (or decrement high I should say) since we don't know what is to the right of mid, it could be anything
                # this means we'd need to check the mid val again, which would be taken care of in the next iteration
                

# this problem's also called the Dutch National Flag Problem

#I initially thought we should maintain 3 pointers and swap in such a way that:
# the first pointer swaps with the second
#second with the third
#and third with the first
#this approach is incredibly convoluted and honestly, wouldn't work
# there are no clear cut boundaries with this method