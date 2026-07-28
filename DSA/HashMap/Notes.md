## What Kinds of Problems Can Be Solved by Hashing?

While Two Pointers and Sliding Windows rely heavily on **order, continuity, and monotonicity** (elements being next to each other or sorted), **Hashing** is the exact opposite.

Hashing shines when you need **O(1) lookups** for elements that are scattered, unsorted, or completely disconnected from each other.

---

### The Fundamental Rule: Instant Lookups & Frequency Tracking

> **Use hashing when you need to remember what you’ve seen before, count frequencies instantly, or check for existence in $O(1)$ time without scanning the whole array again.**

If a problem forces you to repeatedly search through an array to find a specific element, value, or complement, a Hash Map or Hash Set will usually optimize your time complexity from $O(N^2)$ down to $O(N)$.

---

## The 4 Main Hashing Patterns

### Pattern 1: The Complement / "Two Sum" Pattern

Use this when you need to find if a specific pair (or subset) exists that adds up to, multiplies to, or matches a target, but the array is **unsorted**.

* **How it works:** As you iterate through the array, calculate what "complement" you need (e.g., `target - current_element`). Check if that complement is already in your Hash Map. If not, store the current element and move on.
* **When to apply:**
* *"Two Sum"* (in an unsorted array)
* *"Find if there is a subarray with 0 sum"*
* *"Subarray sum equals K"* (Prefix Sum + Hash Map)


* **Key indicator:** Unsorted array + looking for pairs or specific mathematical relationships.

---

### Pattern 2: Frequency Counting & Anagrams

Use this when the frequency or exact count of characters/elements matters more than their order.

* **How it works:** Store elements as keys and their counts as values.
* **When to apply:**
* *"Valid Anagram"* or *"Group Anagrams"*
* *"First unique character in a string"*
* *"Top K frequent elements"*


* **Key indicator:** Words like *"frequency"*, *"count"*, *"permutation"*, or *"rearrange"*.

---

### Pattern 3: Seen Set / Duplicate Detection & Tracking

Use this when you need to check for prior existence or eliminate duplicates instantly.

* **How it works:** Insert elements into a Hash Set as you traverse. If you encounter an element already in the set, you've found your duplicate.
* **When to apply:**
* *"Contains Duplicate"*
* *"Longest Consecutive Sequence"* (store elements in a set to check for sequence starts in $O(1)$)
* *"Intersection of two arrays"*


* **Key indicator:** Checking *"Have I seen this before?"* or finding unique items.

---

### Pattern 4: State Saving / Memoization & Prefix Tracking

Use this when tracking cumulative states (like running sums, bitmasks, or paths) to answer range queries.

* **How it works:** Store the running state as a key and the first occurrence index (or count) as the value.
* **When to apply:**
* *"Continuous Subarray Sum"*
* *"Longest Subarray with Equal Number of 0s and 1s"*


* **Key indicator:** Subarray problems that involve **negative numbers** (where sliding window and two pointers fail because monotonicity is broken).

---

## Quick Decision Flowchart: When to Abandon Two Pointers for Hashing

1. **Are you looking for a subarray/substring, but the array contains negative numbers or breaks monotonicity?**
* $\rightarrow$ **Prefix Sum + Hash Map** (e.g., Subarray Sum Equals K).


2. **Is the data completely unsorted, and sorting it would destroy index requirements or take too much time ($O(N \log N)$)?**
* $\rightarrow$ **Hash Map / Hash Set** for $O(1)$ lookups.


3. **Do you need to keep track of frequencies, counts, or groupings of elements?**
* $\rightarrow$ **Frequency Map**.