```
Input: num = 400
Output: "CD"

Input: num = 58
Output: "LVIII"
Explanation: L = 50, V = 5, III = 3
```

## Step-by-Step Example (1994 → MCMXCIV)

```
Initial number: 1994

1. Check 1000 (M):  1994 ≥ 1000
   - Add "M"
   - Remaining: 994
   Result: "M"

2. Check 900 (CM):  994 ≥ 900
   - Add "CM"
   - Remaining: 94
   Result: "MCM"

3. Check 90 (XC):   94 ≥ 90
   - Add "XC"
   - Remaining: 4
   Result: "MCMXC"

4. Check 4 (IV):    4 = 4
   - Add "IV"
   - Remaining: 0
   Final Result: "MCMXCIV"
```

## Approach

1. **Use Value-Symbol Dictionary**

   - Create a dictionary mapping integer values to Roman symbols
   - Include special combinations (900 -> CM, 400 -> CD, etc.)
   - Sort values in descending order

2. **Greedy Conversion**
   - Start with largest values
   - While number ≥ current value:
     - Add corresponding Roman symbol
     - Subtract value from number
   - Continue until number becomes 0

## Time & Space Complexity

- Time: O(1) - constant time as input is bounded (1-3999)
- Space: O(1) - fixed size dictionary for symbols

## Key Points

- Roman numerals use subtractive notation (IV = 4, IX = 9)
- Must handle special cases (400, 900, etc.)
- Process larger values first
- Dictionary keys must be sorted in descending order

## Edge Cases

- Number = 1 (single symbol)
- Number = 3999 (maximum value)
- Numbers requiring subtractive notation (4, 9, 40, 90, etc.)

## Special Combinations

```
M  = 1000    CM = 900
D  = 500     CD = 400
C  = 100     XC = 90
L  = 50      XL = 40
X  = 10      IX = 9
V  = 5       IV = 4
I  = 1
```
