# This question is leetcode premium, so i got it from neetcode and i solved it myself , no help from anybody
# https://leetcode.com/problems/meeting-rooms-ii/
# https://neetcode.io/problems/meeting-schedule-ii/question
"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # Using 1D differential array (pfix or LIne Sweep)
        mapp = {}
        ans = 0
        for x in intervals:
            L = x.start
            R = x.end
            mapp[L] = 1 + mapp.get(L,0)
            mapp[R] = -1 + mapp.get(R,0)
        # let's convert mapp in sorted list
        keys = sorted(mapp.keys())
        for i in range(1,len(keys)):
            mapp[keys[i]] += mapp[keys[i-1]]
        for x in mapp:
            ans = max(ans,mapp[x])
        return ans