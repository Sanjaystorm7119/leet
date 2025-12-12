# Encode and Decode Strings (Short Notes)

## Problem

Design an algorithm to encode a list of strings to a single string and decode it back.

## Approach (Length-prefixed with delimiter)

- Encode each string as `<len>#<string>` and concatenate all segments.
- During decode, read characters until `#` to get the length, then read the next `length` characters as the original string.

## Why it works

- The length prefix ensures the decoder knows exactly how many characters to read for each string, avoiding ambiguity even if strings contain `#`.

## Complexity

- Time: O(total_chars) — both encode and decode scan each character a constant number of times.
- Space: O(total_chars) for the encoded string and for the output list during decode.

## Implementation notes

- Use a list and `"".join()` to build the encoded string efficiently.
- During decode, parse the length by scanning until `#`, convert to integer, then slice the next `length` characters.
- Avoid printing inside `decode` (debug `print(length)` present in file) — remove for production.

## Edge cases

- Empty list => encode returns empty string; decode returns [].
- Empty strings in list: encode will represent them as `0#` and decode handles them correctly.
- Very large strings: ensure integer conversion and slicing handle sizes (Python handles big ints but watch memory).

## Example

Encode: `['hello','jay']` -> `'5#hello3#jay'`
Decode: `'5#hello3#jay'` -> `['hello','jay']`

## Small improvements

- Remove debug prints (e.g., `print(length)`) from `decode`.
- Add type hints and docstrings for clarity.
- Add unit tests for empty list, strings containing `#`, and strings with unicode characters.
