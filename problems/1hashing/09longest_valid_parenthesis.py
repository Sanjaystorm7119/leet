class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]           
        longest = 0

        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)
            else:  # char == ')'
                stack.pop()
                if not stack:
                    stack.append(i)
                else:     
                    longest = max(longest, i - stack[-1])
        return longest

ans = Solution()
print(ans.longestValidParentheses(")(())"))