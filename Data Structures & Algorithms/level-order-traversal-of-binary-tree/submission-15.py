# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res=[]
        def rec(node,dist):
            if not node:
                return None
            if dist>=len(res):
                res.append([])
            res[dist].append(node.val)
            rec(node.left,dist+1)
            rec(node.right,dist+1)
        rec(root,0)
        return res    

        