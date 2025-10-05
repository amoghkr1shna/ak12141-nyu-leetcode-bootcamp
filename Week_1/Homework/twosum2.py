#from typing import List
#The import statements are usually added by the LeetCode platform, I've added here for reference

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        #for the left/first pointer
        j = len(numbers) - 1
        #for the right/second pointer

        while i!=j:
            #we need to loop through the array/list until the pointers cross over
            if numbers[i] + numbers[j] < target:
                #similar to binary search (low,high,mid)
                #also similar to the merge part of merge sort (and only the merge)
                #the kicker lies in the fact that the array is sorted
                #if the sum of a[i] & a[j] is less than the target, then it means we need to go towards the right
                #since it's increasing order (right = higher values)
                i = i+1

            if numbers[i] + numbers[j] > target:
                j = j-1
                #if the sum of a[i] & a[j] is greater than the target, then it means we've overshot ; we need to go towards the left

            if numbers[i] + numbers[j] == target:
                #if we've found a match, then return the values. Since this problem requires 1-indexing, I'm incrementing by 1
                return [i+1,j+1]


#My initial approach was to use one pointer and use binary search to find the complement, since the array is sorted
#This is too slow (O(n log n)) and not optimal
#The two pointer approach is O(n) and optimal