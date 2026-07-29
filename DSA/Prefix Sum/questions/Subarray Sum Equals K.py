class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # idea from solution page
        count = 0
        pfix = 0
        mapp = {}
        mapp[0] = 1
        for x in nums:
            pfix += x
            # pfix-k is varying
            if pfix - k in mapp:
                count += mapp[pfix - k]

            if pfix in mapp:
                mapp[pfix] = 1 + mapp[pfix]
            else:
                mapp[pfix] = 1
            # mapp[pfix] = 1 + mapp.get(pfix,0)
            # Without .get(), if you tried to do mapp[pfix] = mapp[pfix] + 1 on a brand-new prefix sum, Python would crash immediately because the key doesn't exist yet! .get(pfix, 0) prevents that crash by providing 0 as the starting count.
        return count
