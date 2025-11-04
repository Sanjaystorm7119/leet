# Reverse Linked List

## Problem Statement

Given the head of a singly linked list, reverse the list, and return the reversed list.

## Example

```
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]
```

## Approach

1. **Iterative Solution**

   - Use 3 pointers: prev, curr, and next
   - Initially prev is None, curr points to head
   - For each node:
     - Save next pointer
     - Reverse current pointer
     - Move prev and curr forward

2. **Time & Space Complexity**
   - Time: O(n) where n is number of nodes
   - Space: O(1) as only using pointers

## Key Points

- Edge cases: empty list, single node
- Always save next pointer before modifying current
- Remember to update head at the end
- Careful not to lose references while reversing
