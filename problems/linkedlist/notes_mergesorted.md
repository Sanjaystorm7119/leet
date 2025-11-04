# Merge Two Sorted Lists

## Problem Statement

Merge two sorted singly-linked lists and return it as a single sorted list. The lists should be merged by splicing together the nodes of the first two lists.

## Example

```
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
```

## Approach (Iterative - Dummy Node)

1. Create a dummy node and a tail pointer pointing to it.
2. While both lists are non-empty:
   - Compare `list1.val` and `list2.val`.
   - Append the smaller node to `tail.next` and advance that list.
   - Move `tail` to `tail.next`.
3. After the loop, append the remaining non-empty list to `tail.next`.
4. Return `dummy.next` as the head of merged list.

## Time & Space Complexity

- Time: O(n + m) where n and m are lengths of the two lists.
- Space: O(1) — only pointer rearrangements; no extra list allocations.

## Key Points

- Use a dummy node to simplify head handling.
- Move existing nodes (not values) to avoid extra memory.
- Ensure to attach the leftover list after the main loop.

## Edge Cases

- One or both lists are empty.
- Lists of significantly different lengths.
- All nodes in one list are smaller/larger than all nodes in the other.

## Variant / Recursion

- A recursive solution is possible: pick the smaller head, set its `next` to merge(rest, other), and return it. Recursive depth = O(n+m).

## Quick tip

- When testing, build small linked lists and verify node identities (not only values) to ensure nodes are being reused rather than copied.
