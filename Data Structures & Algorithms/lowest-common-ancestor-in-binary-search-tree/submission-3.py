# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not p or not q:
            return None
        curr=root    
        curr1=p
        curr2=q
        while(curr):
            if curr.val <curr1.val and curr.val<curr2.val:
                curr=curr.right
            elif curr.val >curr1.val and curr.val>curr2.val:
                curr=curr.left
            else:
                return curr               
        