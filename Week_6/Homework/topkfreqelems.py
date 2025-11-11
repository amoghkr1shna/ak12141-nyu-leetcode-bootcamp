from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]: 
        # O(1) time 
        if k == len(nums):
            return nums
        
        count = Counter(nums)   
        return heapq.nlargest(k, count.keys(), key=count.get) 