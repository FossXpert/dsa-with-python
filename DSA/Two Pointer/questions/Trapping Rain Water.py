class Solution:
    def trap(self, height: List[int]) -> int:
        # brute force
        a = [-1] * len(height)
        b = [-1] * len(height)
        ans = 0 
        n = len(height)
        for i in range(n):
            rmax = -1
            for j in range(i + 1, n):
                rmax = max(height[j], rmax)
            a[i] = rmax
        for i in range(n-1,-1,-1):
            lmax = -1
            for j in range(i-1,-1,-1):
                lmax = max(height[j], lmax)
            b[i] = lmax
        for i in range(0, len(a)):
            x = min(a[i],b[i]) - height[i]
            if x > 0:
                ans += x
        return ans

        # optimized solution
        