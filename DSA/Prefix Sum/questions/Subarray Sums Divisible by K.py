class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        # here i am using this idea: https://leetcode.com/discuss/post/5119937/prefix-sum-problems-by-c0d3m-08l9/
        # section 2
        pfix,count,n=0,0,len(nums)
        mapp = {}
        mapp[0] = 1

        for i in range(n):
            pfix+=nums[i]
            mod = (pfix%k + k)%k
            if mod in mapp:
                count += mapp[mod]
            if mod in mapp:
                mapp[mod] = 1 + mapp[mod]
            else:
                mapp[mod] = 1
        return count

# https://leetcode.com/problems/subarray-sums-divisible-by-k