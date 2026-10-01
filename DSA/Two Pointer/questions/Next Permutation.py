class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        # check previous submission for your own code
        # I have used reverse here and in previous submission I used sorted, btw sorting is not required

        index = -1
        n = len(nums)
        for i in range(n - 1, 0, -1):
            if nums[i] <= nums[i - 1]:
                index = i - 1
            else:
                break

        # swapping
        if index == -1:
            nums[n - 1], nums[n - 2] = nums[n - 2], nums[n - 1]
            return

        if index == 0:
            nums.reverse()
            return

        # Need to find out next greater element after nums[index-1] along with index
        # filtering elements
        # nums2 is a tuple, a kind of 2D array
        nums2 = []
        for i in range(index, n):
            if nums[i] > nums[index - 1]:
                nums2.append((nums[i], i))

        # finding min'm element in nums2
        smallest_val, smallest_idx = nums2[0]

        for item in nums2:
            if item[0] <= smallest_val:
                smallest_val, smallest_idx = item

        # swapping nums[index] with nums[smallest_idx] in python way
        nums[index - 1], nums[smallest_idx] = nums[smallest_idx], nums[index - 1]

        # now reversion from nums[index] to last
        nums[index:n] = reversed(nums[index:n])