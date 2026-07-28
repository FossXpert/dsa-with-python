## When to Use Prefix Sum

**Prefix Sum** is a technique used to answer **range sum queries** or track cumulative states in $O(1)$ time after an initial $O(N)$ preprocessing step.

Think of it as keeping a running total as you walk through an array. Instead of re-adding elements every time you need the sum of a range from index $i$ to $j$, you just subtract two precomputed cumulative sums: `Prefix[j] - Prefix[i-1]`.

---

### The Fundamental Rule: Cumulative Tracking & Range Queries

> **Use a prefix sum when a problem asks you to repeatedly find the sum (or product/xor) of elements across various subarrays/ranges, or when you need to know the running balance of elements over time.**

---

## The 3 Main Prefix Sum Patterns

### Pattern 1: Static Range Sum Queries

Use this when you have a fixed array and need to query the sum of elements between indices $L$ and $R$ multiple times.

* **How it works:** Build a prefix array where `prefix[i]` stores the sum of all elements from index $0$ up to $i$. The sum of range $[L, R]$ becomes `prefix[R] - prefix[L-1]`.
* **When to apply:**
* *"Range Sum Query - Immutable"*
* *"Find the equilibrium index of an array"* (where the sum of elements to the left equals the sum to the right).


* **Key indicator:** Multiple queries asking for sums of continuous subsegments in a static array.

---

### Pattern 2: Prefix Sum + Hash Map (The Ultimate Counter-Attack)

Use this when you are dealing with **subarrays**, the array has **negative numbers** (which breaks Sliding Window/Two Pointers), and you need to find a target sum.

* **How it works:** As you compute the running prefix sum, store how many times each prefix sum has appeared in a Hash Map. If `CurrentPrefixSum - Target` exists in your map, you've found valid subarrays.
* **When to apply:**
* *"Subarray Sum Equals K"*
* *"Continuous Subarray Sum"* (using modulo)
* *"Binary subarrays with sum"*


* **Key indicator:** Subarray problems with **negative numbers** or checking if a specific target sum exists without using sliding windows.

---

### Pattern 3: Transforming Arrays & Difference Arrays (Range Updates)

Use this variant when you need to apply many updates to ranges of an array and then find the final values.

* **How it works:** Instead of updating every single element in a range $[L, R]$ (which takes $O(N)$ per update), you mark the start (+val) and the end after $R$ (-val) using a difference array. Then, take the prefix sum at the end to get the final state.
* **When to apply:**
* *"Corporate Flight Bookings"*
* *"Car Pooling"*


* **Key indicator:** Frequent range-update operations followed by final point queries.

---

## Quick Decision Flowchart: When to Use Prefix Sum

1. **Does the problem ask for the sum of a continuous range $[L, R]$ and repeat it many times?**
* $\rightarrow$ **Basic Prefix Sum** ($O(1)$ per query).


2. **Does it ask for subarrays with a specific sum ($K$), but the array contains negative numbers?**
* $\rightarrow$ **Prefix Sum + Hash Map** (since Two Pointers / Sliding Window fail due to lost monotonicity).


3. **Do you need to add a value to an entire range of indices efficiently?**
* $\rightarrow$ **Difference Array + Prefix Sum**.