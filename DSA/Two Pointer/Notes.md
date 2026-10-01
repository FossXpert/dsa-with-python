** General summary of what kind of problem can/ cannot solved by Two Pointers **
Here is the general rule of thumb for when to use **Two Pointers** or **Sliding Window**, along with the key patterns to look for.

---

### The Fundamental Rule: Monotonicity

For two pointers or a sliding window to work, your problem state **must change in a single, predictable direction** when you move a pointer:

> **Moving a pointer in direction $A$ must ALWAYS increase/improve the property.**
> **Moving a pointer in direction $B$ must ALWAYS decrease/reduce the property.**

If moving a pointer could make your metric go **up OR down unpredictably**, two pointers **will not work** (which is why negative numbers broke the subarray sum problem earlier!).

---

## The 4 Main Two-Pointer / Sliding Window Patterns

### Pattern 1: Dynamic Sliding Window (Expand / Shrink)

Use this when you are asked for the **longest, shortest, or number of subarrays/substrings** that satisfy a condition.

* **How it works:**
1. Move `right` to expand the window until the condition becomes valid (or invalid).
2. Move `left` to shrink the window until you regain control.


* **When to apply:**
* *"Find the longest substring with at most $K$ distinct characters"*
* *"Find the minimum size subarray whose sum is $\ge K$"* (only for positive numbers!)


* **Key indicator:** Subsegments or subarrays where expanding **never decreases** the count/sum/size.

---

### Pattern 2: Fixed-Size Sliding Window

Use this when the **window size $K$ is constant**.

* **How it works:**
* Maintain a window of length $K$.
* As you slide right: **Add** `nums[i]` on the right, **Remove** `nums[i - K]` from the left.


* **When to apply:**
* *"Maximum sum of any subarray of size $K$"*
* *"Find all anagrams of a string $P$ in string $S$"*


* **Key indicator:** The problem explicitly specifies a fixed window size $K$.

---

### Pattern 3: Two Pointers Meeting in the Middle (Opposite Ends)

Use this when the array is **sorted** (or can be sorted without breaking the output requirements).

* **How it works:**
* `left = 0`, `right = n - 1`
* If the current combination is too small $\rightarrow$ `left += 1` (increases sum/value).
* If the current combination is too large $\rightarrow$ `right -= 1` (decreases sum/value).


* **When to apply:**
* *"Two Sum in a sorted array"*
* *"Container With Most Water"*
* *"3Sum / 4Sum"*
* *"Valid Palindrome"*


* **Key indicator:** Sorted array + searching for pairs, triplets, or boundaries.

---

### Pattern 4: Fast & Slow Pointers (Cycle Detection)

Use this when dealing with **linked lists, arrays as pointers, or cycles**.

* **How it works:**
* `slow` moves 1 step at a time.
* `fast` moves 2 steps at a time.


* **When to apply:**
* *"Detect cycle in a Linked List"*
* *"Find the middle of a Linked List"*
* *"Find the duplicate number in an array of size $N+1$"*


* **Key indicator:** Linked structures, cyclic dependencies, or finding midpoints without calculating total length first.

---

## Quick Decision Flowchart

When you read an array or string problem, ask yourself:

1. **Is it asking for contiguous subarrays/substrings?**
* **Yes:**
* Is the window size fixed? $\rightarrow$ **Fixed Sliding Window**
* Does expanding always increase the value and shrinking always decrease it? $\rightarrow$ **Dynamic Sliding Window**
* Can the value go up OR down randomly (like negative numbers)? $\rightarrow$ **STOP! Use Prefix Sum + Hash Map or Dynamic Programming.**




2. **Is the array sorted and asking for pairs/triplets?**
* **Yes:** $\rightarrow$ **Two Pointers from opposite ends (`left = 0`, `right = n - 1`)**


3. **Is it a linked list or cyclic traversal?**
* **Yes:** $\rightarrow$ **Fast & Slow Pointers**