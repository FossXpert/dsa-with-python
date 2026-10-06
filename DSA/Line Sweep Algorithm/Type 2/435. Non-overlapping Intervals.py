from functools import cmp_to_key
class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        # trying method 2 according to the previous quesion i did  from line sweep list
        sortedList = sorted(intervals,key=lambda item:item[1])
        n = len(sortedList)
        ans = 0
        prev_end = sortedList[0][1]
        for i in range(1,n):
            if prev_end > sortedList[i][0]:
                ans += 1
            else:
                prev_end = sortedList[i][1]
        return ans
        
# https://leetcode.com/problems/non-overlapping-intervals/