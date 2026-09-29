class NumMatrix:

    def __init__(self, matrix: list[list[int]]):
        self.matrix = matrix
        # calculating prefix sum array with formula mentioned in sheet
        # first declaring a prefix array with size [m+1][n+1] for matrix of size m and n
        row = len(matrix)
        col = len(matrix[0])
        pfix = [[0 for _ in range(col + 1)] for _ in range(row + 1)]

        # now i am using formulae
        # remember arr[] is start from 0,0 pfix is just 1 size more row+1 and col+1
        # original formula is : pfix[i][j] = pfix[i][j-1] + pfix[i-1][j] + pfix[i-1][j-1] + arr[i][j]
        # pfix[i+1][j+1] = pfix[i+1][j] + pfix[i][j+1] - pfix[i][j] + arr[i][j]

        for i in range(row):
            for j in range(col):
                pfix[i + 1][j + 1] = pfix[i + 1][j] + pfix[i][j + 1] - pfix[i][j] + matrix[i][j]
        self.pfix = pfix

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        # writing optimised version because brute force gave me TLE
        # i my self figured out the formulae with paper and pen with a example given in problem descriptio
             
        summ = self.pfix[row2+1][col2+1] - self.pfix[row2+1][col1] - self.pfix[row1][col2+1] + self.pfix[row1][col1]
        return summ


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
