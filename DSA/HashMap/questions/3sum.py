
nums = []
ans []
def threeSum(self, nums: list[int]) -> list[list[int]]:
    for i in range(0, len(nums)):
        tripl1 = nums[i]
        target = 0 - nums[i]
        mapp = {}
        for j in range(0, len(nums)):
            mapp[nums[j]] = j

        for k in range(0, len(nums)):
            x = target - nums[k]
            if x in mapp and k!=i and i!=mapp[x] and k!=mapp[x]:
                ans.append(tripl1,nums[mapp[x]],nums[k])

