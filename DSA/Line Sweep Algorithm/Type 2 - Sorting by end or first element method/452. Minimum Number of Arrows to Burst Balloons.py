class Solution:
    def findMinArrowShots(self, points: list[list[int]]) -> int:
        # Need to see hint as it's my first uestion with this method for line sweep - got idea from here :https://leetcode.com/discuss/post/2166045/line-sweep-algorithms-by-c0d3m-8ebq/
        # use this example to understand : points = [[1, 10], [2, 3], [4, 5]]
        ans = 1
        sortedPoints = sorted(points, key=lambda item: item[1]) # sorting by 2nd element
        prev_end = sortedPoints[0][1]

        for i in range(1, len(points)):
            # if prev_end > sortedPoints[i][0] - to hme ignore krna hai
            if prev_end < sortedPoints[i][0]:
                ans += 1
                prev_end = sortedPoints[i][1]
        return ans

# https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/