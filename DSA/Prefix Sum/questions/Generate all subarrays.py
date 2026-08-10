def findAllSubarraySums(nums: list[int]) -> list[int]:
    all_sums = []
    n = len(nums)
    
    # i is the start of the subarray
    for i in range(n):
        current_sum = 0
        # j is the end of the subarray
        for j in range(i, n):
            current_sum += nums[j]
            all_sums.append(current_sum)   # Stores the sum of nums[i...j]
            
    return all_sums
# we can't find it in o(n) order, we just can't. only in o(n²) it's possible