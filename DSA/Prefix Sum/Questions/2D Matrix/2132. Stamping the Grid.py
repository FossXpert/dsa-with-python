class Solution:
    def possibleToStamp(self, grid: list[list[int]], stampHeight: int, stampWidth: int) -> bool:
        # I was not able to think myself
        # check this file for explanation - 
        # Got idea from the sheet - > https://leetcode.com/discuss/post/5119937/prefix-sum-problems-by-c0d3m-08l9/

        # Step 1: Create a pfix sum array for grid array
        # Step 2: Find the grid with fixed stampHeight and stampWidth whose sum is 0 (refer this question: https://leetcode.com/problems/range-sum-query-2d-immutable/description/)
        # Step 3: If this grid sum is 0, then use 2D differential array method to mark cells in other matrix given in tutorial
        # Step 4: Check every cells if it's empty return false,else return true

        # Step 1: Initialize dimensions and prefix sum matrices
        row = len(grid)
        col = len(grid[0])
        
        # pfix: Stores 2D prefix sums of the original grid to quickly query subgrid sums in O(1) time
        pfix = [[0 for _ in range(col+1)] for _ in range(row+1)]
        
        # pfix2: Acts as our 2D difference array (with extra padding to handle boundary updates safely)
        pfix2 = [[0 for _ in range(col+2)] for _ in range(row+2)] 

        # Populate the 2D prefix sum table for the grid
        for i in range(0,row):
            for j in range(0,col):
                pfix[i+1][j+1] = pfix[i+1][j] + pfix[i][j+1] - pfix[i][j] + grid[i][j]

        # Step 2: Iterate over all possible top-left corners where a stamp can fit
        for i in range(0,row - stampHeight + 1):
            for j in range(0,col - stampWidth + 1):
                # Define 1-based boundaries of the current stamp placement rectangle
                r1 = i + 1
                c1 = j + 1
                r2 = i + stampHeight
                c2 = j + stampWidth

                # Query the subgrid sum in O(1) using the prefix sum table
                isGridSumZero = pfix[r2][c2] - pfix[r1-1][c2] - pfix[r2][c1-1] + pfix[r1-1][c1-1]

                # If the sum is 0, it means the area is completely empty (no obstacles)
                if isGridSumZero == 0:
                    # Step 3: Apply the 2D Difference Array (Offline Range Update) technique
                    # This marks the entire stamp region [r1, c1] to [r2, c2] efficiently in O(1)
                    pfix2[r1][c1] += 1
                    pfix2[r1][c2+1] -= 1
                    pfix2[r2+1][c1] -= 1
                    pfix2[r2+1][c2+1] += 1
        
        # Step 4 part A: Compute the 2D prefix sum of the difference array (pfix2)
        # This reconstructs how many times each cell is covered by a valid stamp
        for i in range(1,row+2):
            for j in range(1,col+2):
                pfix2[i][j] = pfix2[i][j-1] + pfix2[i-1][j] - pfix2[i-1][j-1] + pfix2[i][j]

        # Step 4 part B: Validate if all initially empty cells (grid[i][j] == 0) are covered at least once
        for i in range(0,row):
            for j in range(0,col):
                # If an empty cell has a coverage count of 0, it's impossible to stamp the grid
                if grid[i][j] == 0 and pfix2[i+1][j+1] == 0:
                    return False
                    
        # If all empty cells are successfully covered, return True
        return True

# https://leetcode.com/problems/stamping-the-grid/



