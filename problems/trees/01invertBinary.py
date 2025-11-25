from typing import Optional
class TreeNode:
    def __init__(self, left=None , right=None , val = 0):
        self.left = left
        self.right = right
        self.val = val

class Solution:
    def invert_tree(self, root:Optional[TreeNode])-> Optional[TreeNode]:
        if not root :
            return
        else :
            root.left , root.right  = root.right , root.left
            self.invert_tree(root.left)
            self.invert_tree(root.right)
            return root
        
        