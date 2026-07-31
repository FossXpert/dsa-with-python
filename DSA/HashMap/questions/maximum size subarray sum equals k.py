# https://leetcode.com/problems/maximum-size-subarray-sum-equals-k/description/
#  i solved this here : https://algo.monster/liteproblems/325#editor

def maximum_size_subarray_sum_equals_k(nums: list[int], k: int) -> int:
    # WRITE YOUR BRILLIANT CODE HERE
    mapp = {}
    mapp[0] = 0
    pfix = 0
    n = len(nums)
    count = 0

    for i in range(n):
        pfix+=nums[i]
        if pfix-k in mapp:
            count = max(count,i+1 - mapp[pfix-k])
        if pfix in mapp:
            mapp[pfix] = min(mapp[pfix],i+1)
        else:
            mapp[pfix] = i+1
        
        
    return count

if __name__ == "__main__":
    nums = [int(x) for x in input().split()]
    k = int(input())
    res = maximum_size_subarray_sum_equals_k(nums, k)
    print(res)
