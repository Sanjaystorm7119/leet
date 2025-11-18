# Minimum Distance Among Three Occurrences

## Problem Statement

Given an array of integers `nums`, find the minimum total pairwise distance among any three occurrences of the same number. If no number appears at least three times, return -1.

## Example

```
Input: nums = [1,4,3,1,5,9,1,2,3]
Output: 6
Explanation: Indices of 1 are [0, 3, 6]. Distances = |0-3| + |3-6| + |6-0| = 3 + 3 + 6 = 12 (note: see approach for minimizing selection)
```

## Approach

1. Build an index map (value -> list of indices where it occurs).
2. For each value with at least 3 occurrences, slide a window of size 3 over its index list.
3. For each triple of indices (a, b, c) compute the total pairwise distance: |a-b| + |b-c| + |c-a|.
4. Track the minimum such distance across all values.
5. If no triple found, return -1.

Notes on formula: For indices sorted a ≤ b ≤ c, the pairwise sum simplifies to 2*(c - a). So you can compute dist = 2 * (c - a) which is faster than summing three absolute differences.

## Time & Space Complexity

- Time: O(n) to build the index map plus O(k) over all occurrences when sliding windows are used — overall O(n).
- Space: O(n) for the positions map.

## Key Points

- Store indices for each number while scanning once.
- Only values with ≥ 3 occurrences matter.
- Because indices are naturally collected in increasing order, triples (a,b,c) are already sorted.
- Use the simplified formula dist = 2 \* (c - a) for speed and clarity.

## Edge Cases

- No number appears 3 times -> return -1.
- Large arrays where many values have multiple occurrences (ensure linear memory/time behavior).
- Values clustered together vs spread out — sliding window ensures best local triple is considered.

## Quick Tip

- If you also need to return the indices of the best triple, keep track of the (a,b,c) when updating the minimum.
