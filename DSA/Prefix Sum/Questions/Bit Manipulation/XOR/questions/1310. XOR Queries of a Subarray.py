class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        # ^ - xor symbol
        # optimising by using xor property : 
        # Self-Inverse: Applying the XOR operation with the same value twice cancels it out. If you take a number A and XOR it with B, and then XOR the result with B again, you get A back i.e (A ^ B) ^ B = A or (A ^ B) ^ A = B

        xorArr,ans=[],[]
        n = len(arr)
        xorArr.append(arr[0])

        for i in range(1, n):
            xorArr.append(arr[i] ^ xorArr[i - 1])

        for left, right in queries:
            if left == 0:
                ans.append(xorArr[right])
            else:
                ans.append(xorArr[right] ^ xorArr[left - 1])

        return ans

# https://leetcode.com/problems/xor-queries-of-a-subarray/description/