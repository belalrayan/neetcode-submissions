# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        def dfs(node,left_max,right_min):
            if not node:
                return True

            if node.val<=left_max or node.val>=right_min:
                return False
                
            return dfs(node.left,left_max,node.val)and dfs(node.right,node.val,right_min)
        return dfs(root,float('-inf'),float('inf'))        

        