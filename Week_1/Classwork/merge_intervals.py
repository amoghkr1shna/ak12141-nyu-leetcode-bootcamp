class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        merged = []
        intervals.sort(key=lambda x: x[0])
        # lambda takes the first element of each interval for sorting
        # it doesn't take the first interval all together, only the first element
        # eg. if i/p: [[1,3], [2,6], [8,10], [15,18]], then x would be:
        # [1,3] -> 1, [2,6] -> 2, [8,10] -> 8, [15,18] -> 15
        # time complexity of internal sort fn is O(nlogn)
        prev = intervals[0]
        # prev = [1,3]

        for interval in intervals[1:]:
            #intervals[1:] means we start from the interval at index 1
            #in the example, it's [2,6], [8,10], [15,18]
            if interval[0] <= prev[1]:  # Overlap
                # 2 <= 3, 
                prev[1] = max(prev[1], interval[1])  # Merge
                # prev[1] = max(3,6) -> prev = [1,6]
            else:
                merged.append(interval)  # No overlap, add to result
        merged.append(prev)  # Add the last interval
        return merged