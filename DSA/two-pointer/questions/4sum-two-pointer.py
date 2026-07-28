class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        nums.sort()
        for l in range(len(nums) - 3):
            if l > 0 and nums[l] == nums[l - 1]:
                continue
            for k in range(l + 1, len(nums) - 2):
                if k > l + 1 and nums[k] == nums[k - 1]:
                    continue
                i = k + 1
                j = len(nums) - 1
                targett = target - nums[k] - nums[l]
                while i < j:
                    x = nums[i] + nums[j]
                    if x == targett:
                        ans.append([nums[l], nums[k], nums[i], nums[j]])
                        while i < j and nums[i] == nums[i + 1]:
                            i += 1
                        while i < j and nums[j] == nums[j - 1]:
                            j -= 1
                        i += 1
                        j -= 1
                    if x > targett:
                        j -= 1
                    if x < targett:
                        i += 1
        return ans
# https://leetcode.com/problems/4sum/