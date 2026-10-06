class Solution:
    def maximalSquare(self, matrix: list[list[str]]) -> int:
        
        # I was not able to solve my self, took help from this discussion - https://leetcode.com/problems/maximal-square/description/comments/2732103/
        # and from this comment: https://leetcode.com/problems/maximal-square/description/comments/1567477/
        # so basically we cannot use prefix sum or 2D differetial array instead we are using DP (DYnamic prog)

        row = len(matrix)
        col = len(matrix[0])
        ans = 0

        dp = [[0 for _ in range(col)] for _ in range(row)]

        # filling the 1st row and col equal to 1 if matrix 1st row-col  = 1

        for j in range(col):
            if matrix[0][j] == "1":
                dp[0][j] = 1
        for i in range(row):
            if matrix[i][0] == "1":
                dp[i][0] = 1

        # now iam comparing in matrix
        for i in range(1,row):
            for j in range(1,col):
                if matrix[i][j] =="1":
                    if matrix[i-1][j-1] == "1" and matrix[i-1][j] == "1" and matrix[i][j-1] == "1":
                        dp[i][j] = 1 + min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])
                    else:
                        dp[i][j] = 1 # use paper and pen and see, if somewhere is 1 in matrix then offcourse there wiill be atleast area of 1 square will be present, that's why i am initializing the frst row and col same as matrix first

        
        for i in range(row):
            for j in range(col):
                ans = max(ans,dp[i][j])
        return ans * ans

# https://leetcode.com/problems/maximal-square/