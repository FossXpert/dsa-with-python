class Solution:
    # def twoSum(self, nums: List[int], target: int) -> List[int]:
    #     # O(n2)
    #     ans=[]
    #     for i in range(0,len(nums)):
    #         for j in range(i+1,len(nums)):

    #             if nums[i] + nums[j] == target:
    #                 ans.append(i)
    #                 ans.append(j)
    #                 return ans

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #O(n)
        mapp = {}
        for i in range(0, len(nums)):
            mapp[nums[i]] = i

        ans = []
        for i in range(0, len(nums)):
            x = target - nums[i]
            if x in mapp and i != mapp[x]:
                ans.append(i)
                ans.append(mapp[x])
                return ans

        return ans
        
# https://leetcode.com/problems/two-sum/