# https://leetcode.com/problems/insert-interval/description/
# solve it again - good question

from sortedcontainers import SortedDict
class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        # basic question which can be solved wiht the help of 1D differential method
        # optimized witht he help of line sweep algo page solution - https://leetcode.com/discuss/post/2166045/line-sweep-algorithms-by-c0d3m-8ebq/

        # Learning hai isme, like how to handle 1st and last elemnt in one go
        mapp = SortedDict()
        L = newInterval[0]
        R = newInterval[1]
        mapp[L] = 1 + mapp.get(L,0)
        mapp[R] = -1 + mapp.get(R,0)

        for i in range(len(intervals)):
            L = intervals[i][0]
            R = intervals[i][1]
            mapp[L] = 1 + mapp.get(L,0)
            mapp[R] = -1 + mapp.get(R,0)

        keys = mapp.keys()
        result = []
        count = 0
        for i in range(0,len(mapp)):
            if count == 0:
                first = keys[i]
            count += mapp[keys[i]]
            if count == 0:
                last = keys[i]
                result.append([first,last])
        return result
