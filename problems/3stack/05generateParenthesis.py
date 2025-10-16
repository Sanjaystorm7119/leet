class Solution:
    def generateParenthesis(self , num : int)-> list[str] :
        stack = []
        res = []
        def backtrack(openN,closeN):
            if openN == closeN == num :
                res.append("".join(stack))
                print(res)
                return
            if openN < num :
                stack.append("(")
                backtrack(openN+1 ,closeN)
                stack.pop()
            if closeN < openN :
                stack.append(")")
                backtrack(openN ,closeN+1)
                stack.pop()
        backtrack(0,0)
        return res
        
ans = Solution()
print(ans.generateParenthesis(3))

