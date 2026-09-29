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
