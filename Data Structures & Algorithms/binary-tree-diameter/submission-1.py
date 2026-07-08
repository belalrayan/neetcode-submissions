# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter=0
        def helper(curr):
            if not curr:
                return 0
            
            left=helper(curr.left)
            right=helper(curr.right)
            self.diameter=max(left+right,self.diameter)
            return 1+max(left,right)
        helper(root)
        return self.diameter    

    
            