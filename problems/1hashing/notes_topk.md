# Top K Frequent Elements (Short Notes)

## Problem

Given an integer array `nums` and an integer `k`, return the `k` most frequent elements.

## Approach (Bucket sort by frequency)

- Count frequency of each number using a hashmap/dictionary.
- Create an array of lists `buckets` of size `n+1` where index `i` holds numbers with frequency `i`.
- Populate buckets using the frequency map.
- Iterate buckets from high frequency to low, collecting numbers until you have `k` elements.

## Complexity

- Time: O(n) average — counting is O(n), distributing into buckets O(n), scanning buckets O(n).
- Space: O(n) for the frequency map and buckets.

## Notes on Implementation

- Using a bucket array avoids full sorting and gives linear time.
- If `k` is small relative to `n`, a min-heap of size `k` is an alternative: O(n log k) time.
- The example implementation prints the buckets for debugging; remove prints in production.
- Handle edge cases: if `k == 0` return `[]`; if `k >=` number of unique elements, return all unique elements.

## Alternative Approaches

- Sorting unique elements by frequency: O(n log n).
- Min-heap (priority queue) keeping top `k`: O(n log k).

## Example (from file)

Input: `nums = [1,1,2,3,4,5,4]`, `k = 5` -> Output: `[1,4,2,3,5]` (order among same-frequency elements may vary)

## Small improvement suggestions

- Rename `in_list` to `buckets` for clarity.
- Avoid printing large structures; return results directly.
- Consider stable ordering requirement if needed (not required by problem).
