# Reverse Polish Notation (RPN) Notes

## What is RPN?

- Also known as postfix notation
- Mathematical expression where operators follow their operands
- Example: `"2 3 +" means "2 + 3"`
- No parentheses needed - order is determined by position

## Examples

Regular → RPN

- `3 + 4` → `3 4 +`
- `(3 + 4) × 5` → `3 4 + 5 ×`
- `3 + 4 × 5` → `3 4 5 × +`

## Solution Strategy

1. Use a stack to process tokens
2. For each token:
   - If number: push to stack
   - If operator: pop two numbers, apply operator, push result
3. Final answer is the last number in stack

## Time & Space Complexity

- Time: O(n) - process each token once
- Space: O(n) - stack storage in worst case

## Common Pitfalls

1. Stack order for subtraction/division
   - First popped is second operand
   - Example: `5 3 -` means `5 - 3`
2. Converting strings to integers
3. Handling division with negative numbers
