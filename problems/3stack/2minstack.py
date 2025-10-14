class Solution:
    def __init__(self):
        self.stack = []
        self.min_stack = []
    
    def push(self , val : int) -> None :
        self.stack.append(val)
        val = min(val , self.min_stack[-1] if self.min_stack else val)
        self.min_stack.append(val)
    def pop(self)-> None :
        self.min_stack.pop()
        self.stack.pop()
    def top(self)-> None:
        return self.stack[-1]
    def get_min(self)-> None:
        return self.min_stack[-1]

ans = Solution()
print(ans.push(1))
print(ans.push(2))
print(ans.push(3))

print(ans.get_min())
print(ans.top())

