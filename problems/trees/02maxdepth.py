from typing import Optional
class TreeNode:
    def __init__(self, left: None , right : None , val = 0):
        self.left = left
        self.right = right
        self.val = val
    
class Solution:
    def max_depth(self , root: Optional[TreeNode]) -> int:
        if not root :
            return 0
        else :
            left = self.max_depth(root.left)
            right = self.max_depth(root.right)
            return 1 + max(left,right) 

        