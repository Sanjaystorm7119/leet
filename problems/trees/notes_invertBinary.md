# Invert Binary Tree Notes

## Problem

Invert a binary tree by swapping left and right children at every node.

## Approach

**Recursive DFS (Depth-First Search)**

- Base case: If node is null, return
- Swap left and right children
- Recursively invert left subtree
- Recursively invert right subtree

## Time & Space Complexity

- **Time:** O(n) - Visit each node once
- **Space:** O(h) - Recursion stack depth (h = height)

## Key Points

- Simple recursive approach: swap children, then recurse on both subtrees
- Post-order traversal (process children before parent)
- Works bottom-up, inverting deeper levels first
