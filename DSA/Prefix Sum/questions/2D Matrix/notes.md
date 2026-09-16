To create a 2D matrix of size $(n+1) \times (m+1)$ in Python (often used in Dynamic Programming problems), you should use a **list comprehension**.

Here is the correct and safest way to do it:

### The Correct Way (Using List Comprehension)

```python
n = 3
m = 4

# Creates a matrix with (n + 1) rows and (m + 1) columns, initialized with 0
dp = [[0 for c in range(m + 1)] for r in range(n + 1)]

print(len(dp))     # Number of rows = 4 (n + 1)
print(len(dp[0]))  # Number of columns = 5 (m + 1)

```

---

### ⚠️ A Common Mistake to Avoid!

Never initialize a 2D list using multiplication like this:

```python
# ❌ DON'T DO THIS FOR 2D ARRAYS
dp = [[0] * (m + 1)] * (n + 1)

```

**Why is this a trap?**
Multiplication (`*`) copies **references**, not independent objects. It will create a single list for columns and reuse that *exact same list* for every single row. If you change a value in one row (e.g., `dp[0][1] = 5`), it will unexpectedly change in all other rows too!

Using the list comprehension (`[[0 for c in range(...)] for r in range(...)]`) ensures every row is a brand-new, independent list in memory.