# Maximum Depth of Binary Tree Notes

## Problem

Find the maximum depth (height) of a binary tree - longest path from root to leaf node.

## Approach

**Recursive DFS (Depth-First Search)**

- Base case: If node is null, return 0
- Recursively find max depth of left subtree
- Recursively find max depth of right subtree
- Return 1 + max of left and right depths

## Time & Space Complexity

- **Time:** O(n) - Visit each node once
- **Space:** O(h) - Recursion stack depth (h = height)

## Key Points

- Post-order traversal (process children before parent)
- Returns 0 for empty tree, 1 for single node
- Works bottom-up, combining results from subtrees
