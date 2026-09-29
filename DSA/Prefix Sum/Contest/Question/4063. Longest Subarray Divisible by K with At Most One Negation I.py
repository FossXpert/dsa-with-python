class Solution:
    def longestSubarray(self, nums: list[int], k: int) -> int:
        # 1st i thought i can solve this question with the help of https://rb.gy/cguzpa this question concept, also check my prev submission, it was not passing at some test case

        # then for this n2 approach , i don't have to go through map and all, i have to use on2 and calculate sum of all subarray - here is how we can generate all subarrays (https://tinyurl.com/2khp2md8)

        # 1st condn = sum%k == 0 (just calculate length)
        # 2nd condn = (sum-2x)%k = 0 => sum%k = 2x%k
        # [-7,-4] - goated test case

        # Solution reffered :  https://leetcode.com/problems/longest-subarray-divisible-by-k-with-at-most-one-negation-i/solutions/8541513/easy-solution-reverse-modulo-by-abhishek-sb8j https://leetcode.com/problems/longest-subarray-divisible-by-k-with-at-most-one-negation-i/solutions/8541513/easy-solution-reverse-modulo-by-abhishek-sb8j

        count, n = 0, len(nums)
        for i in range(n):
            summ = 0
            mapp = {}
            for j in range(i, n):
                summ += nums[j]
                rem1 = (summ % k + k) % k
                # 1
                if rem1 == 0:
                    count = max(count, j - i + 1)
                # 2
                x = nums[j]
                rem2 = (((x * 2) % k) + k) % k
                mapp[rem2] = 1
                if rem1 in mapp:
                    count = max(count, j - i + 1)

        return count
# https://leetcode.com/problems/longest-subarray-divisible-by-k-with-at-most-one-negation-i/