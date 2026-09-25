class Solution:
    def maximumPopulation(self, logs: list[list[int]]) -> int:
        # I am using 1D-Differential array method(see prefix sum page) to optimise it, let's see if it pass or fail
        # this question comes in category of line sweep, but i am using my previous knowledge to solve it, i wil learn it later then i will apply that technique
        # concept used form this page - https://leetcode.com/discuss/post/5119937/Prefix-Sum-Problems/
        mapp = {}
        for i in range(1950,2051):
            mapp[i] = 0
        n = len(logs)
        for i in range(n):
            L = logs[i][0]
            R = logs[i][1]
            
            mapp[L] += 1
            mapp[R] -= 1
        for i in range(1951,2051):
            mapp[i] += mapp[i-1]

        ans = 0
        year = 1950

        for x in mapp:
            if ans < mapp[x]:
                ans = mapp[x]
                year = x
        return year

