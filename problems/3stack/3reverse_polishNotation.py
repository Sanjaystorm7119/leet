class Solution:
    def evalRPN(self, elements : list[str]):
        char_list = []
        operators = {
                    "+": lambda a, b: a + b,
                    "-": lambda a, b: a - b,
                    "*": lambda a, b: a * b,
                    "/": lambda a, b: int(a / b)
                    }
        for char in elements:
            if char not in operators:
                char_list.append(int(char))
            else:
                num2 = char_list.pop()
                num1 = char_list.pop()
                char_list.append(operators[char](num1,num2))

        return char_list[-1]    
    
ans = Solution()
print(ans.evalRPN(["2","1","/","3","*"]))

                    