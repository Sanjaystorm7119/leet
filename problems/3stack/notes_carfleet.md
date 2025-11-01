Goal: Determine how many car fleets will arrive at the target

Problem summary:

- Cars have starting positions and speeds and head toward a target position
- A car catches up to a slower car ahead and they form a "fleet" that travels together at the slower car's speed
- We need to count how many distinct fleets arrive at the target

Approach:

1. Pair positions with speeds and sort cars by starting position descending (closest to target first)
2. For each car compute time to reach target: (target - position) / speed
3. Iterate from closest to farthest:
   - Maintain a variable `slowest_time` (time of the current leading fleet)
   - If current car's time > slowest_time → it cannot catch up and forms a new fleet; update slowest_time
   - Else current car catches up and becomes part of the existing fleet (do nothing)
4. Count how many times we formed a new fleet

Complexity:

- Time: O(n log n) due to sorting
- Space: O(n) for pairs or O(1) extra if sorting in-place

Example:

- target = 12
- positions = [10, 8, 0, 5, 3]
- speeds = [2, 4, 1, 1, 3]
  Times to target: [1, 1, 12, 7, 3]
  Sorted by position desc → times considered: [1 (pos10), 1 (pos8), 7 (pos5), 3 (pos3), 12 (pos0)]
  Fleets formed: 3

Edge cases:

- No cars → 0 fleets
- Single car → 1 fleet if position < target
- Cars already past the target → ignore or treat as 0-time
- Equal times → simultaneous arrival counts as separate fleets only if they don't catch up before target

Notes:

- Using descending position ensures we process cars that could be caught by those behind them
- Floating point division is fine; use careful comparison for equality if needed
- This is a greedy solution that's easy to implement and efficient
