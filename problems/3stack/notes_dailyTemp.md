Goal: Find number of days to wait until a warmer temperature for each day

Approach: Use monotonic decreasing stack to track temperatures

- Stack stores pairs of [temperature, index]
- Compare current temperature with stack top's temperature using stack[-1][0]
- When warmer temp found, calculate days difference using indices

Stack Strategy:

1. For each temperature:
   - While stack not empty and current temp > stack[-1][0]:
     - Pop [stackTemp, stackInd] pair from stack
     - Calculate days difference (current_index - stackInd)
   - Push [current_temp, current_index] pair to stack

Complexity:

- Time: O(n) - each element pushed/popped at most once
- Space: O(n) - for stack in worst case (decreasing temperatures)

Example: [73, 74, 75, 71, 69, 72, 76, 73]
Result: [1, 1, 4, 2, 1, 1, 0, 0]
Process:

- 73 → stack[[73,0]]
- 74 (warmer) → pop [73,0], result[0]=1, push [74,1]
- 75 (warmer) → pop [74,1], result[1]=1, push [75,2]
- 71 (cooler) → stack[[75,2], [71,3]]
  And so on...

Edge cases:

- Last element always 0 (no future days)
- Decreasing temperatures → all zeros
- Single temperature → [0]

Notes: Efficient solution using stack to avoid nested loops
