class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        num = numbers
        j = len(num)-1
        i=0
        while(i<j):
            x = num[i] + num[j]
            if x == target:
                return [i+1,j+1]
            if x > target:
                j-=1
            if x < target:
                i+=1
        return [-1,-1] 

# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/