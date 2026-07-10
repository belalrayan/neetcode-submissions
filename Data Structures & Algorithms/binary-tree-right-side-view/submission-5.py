# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res=[]

        def rec(node,dist):
            if not node:
                return None
            if dist>=len(res):
                res.append(node.val)

            rec(node.right,dist+1)
            rec(node.left,dist+1)
        rec(root,0)
        return res        
        