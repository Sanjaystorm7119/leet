Goal: Generate all valid combinations of n pairs of parentheses

Approach: Use backtracking with stack to build valid combinations

- Track count of open and closed parentheses
- Use recursive backtracking to explore all valid possibilities
- Maintain balance: closed count must never exceed open count

Key Rules:

1. Can add open parenthesis if open count < n
2. Can add close parenthesis if close count < open count
3. Valid combination found when open = close = n

Stack operations:

- append("(") or append(")") to add parenthesis
- pop() to backtrack and try different combinations
- join stack when valid combination found

Complexity:

- Time: O(4^n/√n) - Catalan number sequence
- Space: O(n) for recursion stack depth

Example: n=2 generates ["(())", "()()"]
Process:

1. Start: ""
2. Add (: "("
3. Branch:
   - Add (: "((" → "(())"
   - Add ): "()" → "()()"

Edge cases:

- n=0 → returns [""]
- n=1 → returns ["()"]

Notes: Clean implementation using recursion; could add input validation
