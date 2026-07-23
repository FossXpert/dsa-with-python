class Solution:
    def trap(self, height: List[int]) -> int:
        # optimised(with two pointer)
        # two pointer help in solve it in O(1) space
        ans = 0
        n = len(height)

        if n < 3:
            return ans
        # 1. calculate left_max
        leftMax, rightMax = height[0], height[n - 1]
        left, right = 0, n - 1

        while left < right:
            if leftMax < rightMax:
                left += 1
                leftMax = max(leftMax, height[left])
                ans += leftMax - height[left]
            else:
                right -= 1
                rightMax = max(rightMax, height[right])
                ans += rightMax - height[right]
                
        return ans
        # optimized solution