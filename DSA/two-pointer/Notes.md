** General summary of what kind of problem can/ cannot solved by Two Pointers **
link  - https://leetcode.com/problems/subarray-sum-equals-k/solutions/301242/general-summary-of-what-kind-of-problem-3py46

Now let's generalize the characteristics of the problems that can be solved by two pinters. The summary is simple:

1. If a wider scope of the sliding window is valid, the narrower scope of that wider scope is valid  - must hold
2. If a narrower scope of the sliding window is invalid, the wider scope of that narrower scope is invalid - must hold

With 2 rules above hold, we are able to optimize the brute-force solution to two pointers solution.

I just show you what kind of question can be solved by two pointers by using some very simple Induction Reasoning. Now let me show you why this problem cannot be solved by two pointers. Like I said, If this problem doesn't meet the creteria that two pointer technique, it cannot be solved with two pointers.

In this specific problem, rule 1 doesn't hold, because I can find a specific case such that it doesn't hold, e.g., if K is 3, 1,1,1 sum is 3, so 1,1,1, is valid, but 1,1 sum is 2 which means 1,1 is invalid, so rule 1 breaks.

Rule2 doesn't hold, either, because I can find a specific case such that it doesn't hold, e.g., if K is 2, 1,1,1 sum is 3, so 1,1,1, is invalid, but 1,1,1,-1 sum is 2 which means 1,1,1,-1 is valid, so rule 2 breaks.