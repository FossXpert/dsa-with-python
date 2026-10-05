to learn about line sweep(1D differential array) - see this page
-  https://www.google.com/url?q=https://leetcode.com/discuss/study-guide/5119937/Prefix-Sum-Problems&sa=D&source=editors&ust=1771796157530153&usg=AOvVaw2K5kf51uFnSZSR8j2NuUWC

1. Python code for sorting with 2nd element
```python
intervals = [[1, 4], [3, 5], [0, 2]]

# Sort by end time (index 1)
intervals.sort(key=lambda x: x[1])
# Result: [[0, 2], [1, 4], [3, 5]]

```
```python
# A list of [x, y] coordinates
points = [[3, 9], [1, 5], [2, 1]]

# Sort by the 1st element (index 0, which is x)
points.sort(key=lambda item: item[0])

print(points)
# Output: [[1, 5], [2, 1], [3, 9]]
```