class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        dic = {"+","-","*","/"}
        stack = []
        for char in tokens:
            if char not in dic:
                stack.append(int(char))
            else:
                num2 = stack.pop()
                num1 = stack.pop()
                if char == "+":
                     stack.append(num1+num2)
                elif char == "-":
                    stack.append(num1-num2)
                elif char == "*":
                    stack.append(num1*num2)
                else :
                    stack.append(int(num1/num2))
        return stack[-1]
    
ans = Solution()
print(ans.evalRPN(["2","1","/","3","*"]))
                