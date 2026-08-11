class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        # I was not able to solve on my own, got idea from here: https://leetcode.com/problems/make-sum-divisible-by-p/description/comments/2656367/
        # i used example while solving [6,3,2,5,10,11,12], p = 9
        pfix,n = 0,len(nums)
        count = n
        arrSum = sum(nums)
        rem = arrSum%p
        if rem == 0:
            return 0
        
        mapp = {}
        mapp[0] = 0
        for i in range(n):
            pfix+=nums[i]
            pfixRem = pfix % p

            targetRem = (pfixRem - rem + p)%p #negative o positive bnane ke liye
            if targetRem in mapp:
                count = min(count,i+1 - mapp[targetRem])

            # remeber max ke liye iska ulta jo use hota tha min ke liye jaruri nahi hai because left to right move krrhe hm to i+1 hmesha largest hi hoga

            # if pfixRem in mapp:
            #     mapp[pfixRem] = max(i+1,mapp[pfixRem])
            # else:
            mapp[pfixRem] = i+1
        
        if count<n:
            return count
        else: 
            return -1
        
#    https://leetcode.com/problems/make-sum-divisible-by-p 
        

        

