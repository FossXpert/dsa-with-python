// https://leetcode.com/problems/insert-interval/

// The Core Approach (3 Phases)
// Since the original intervals are already sorted by their start times, you can solve this efficiently in a single pass by breaking the process down into three phases:

// 1. Add everything that comes BEFORE the new interval:
// Any existing interval that ends before our new interval even starts has no overlap. We can just add them straight to our result list.

// 2. Merge all overlapping intervals:
// Once we hit an interval that overlaps with our newInterval, we keep merging them. An overlap happens if the current interval starts on or before our new interval ends. While they overlap, we expand the boundaries of our newInterval to cover everything from the minimum start time to the maximum end time.

// 3. Add everything that comes AFTER the new interval:
// Once we pass the overlap zone, any remaining intervals can be added as-is because they start after our newly merged interval ends.

class Solution {
public:
    vector<vector<int>> insert(vector<vector<int>>& intervals,
                               vector<int>& newInterval) {
        // I was not able to solve own my own, 2nd case i failed to think
        int n = intervals.size();
        vector<vector<int>> result;

        // Phase 1: Add all intervals that end before newInterval starts
        int i = 0;
        while (i < n and intervals[i][1] < newInterval[0]) {
            result.push_back(intervals[i]);
            i++;
        }
        // Phase 2: Merge all overlapping intervals with newInterval
        while (i < n and intervals[i][0] <= newInterval[1]) {
            newInterval[0] = min(newInterval[0], intervals[i][0]);
            newInterval[1] = max(newInterval[1], intervals[i][1]);
            i++;
        }
        result.push_back(newInterval);
        // Phase 3: Add all remaining intervals that start after newInterval ends, i.e; intervals[i][0] > newInterval[1]
        while(i<n){
            result.push_back(intervals[i]);
            i++;
        }
        return result;
    }
};