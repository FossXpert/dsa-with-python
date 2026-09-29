class Solution:
    def maxScore(self, grid: List[List[int]]) -> int:
        # Not able to think own by own, didn't tried because I thought it will be solved By DP
        # SO took help form this page -> https://leetcode.com/discuss/post/5119937/prefix-sum-problems-by-c0d3m-08l9/#section-3
        # also referred these comments :https://leetcode.com/problems/maximum-difference-score-in-a-grid/description/comments/2395894/
        # and this comment : https://leetcode.com/problems/maximum-difference-score-in-a-grid/description/comments/3477384/

        row = len(grid)
        col = len(grid[0])

        dp = [[-1 for _ in range(col)]for _ in range(row)]
        dp[0][0] = grid[0][0]
        # pfix[i][j] = dp[i][j] =  dp[i][j] stores minimum value of all cels grid[l][k] where l <= i and k<= j 
        # I am creating prefix min matrix

        # Initializing 1st row and column
        for j in range(1,col):
            dp[0][j] = min(dp[0][j-1],grid[0][j])
        for i in range(1,row):
            dp[i][0] = min(dp[i-1][0],grid[i][0])

        for i in range(1,row):
            for j in range(1,col):
                dp[i][j] = min(dp[i][j-1], dp[i-1][j], grid[i][j])
        ans = -100000

        for j in range(1,col):
            ans = max(ans,grid[0][j] - dp[0][j-1])
        for i in range(1,row):
            ans = max(ans,grid[i][0] - dp[i-1][0])

        for i in range(1,row):
            for j in range(1,col):
                ans = max(ans, grid[i][j] - min(dp[i-1][j],dp[i][j-1]))

        return ans

# https://leetcode.com/problems/maximum-difference-score-in-a-grid/