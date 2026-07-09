# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res=[]
        def levelOrderRec(node,dist):
            if not node:
                return
            if len(res)<dist:
                res.append([])
            res[dist-1].append(node.val)
            levelOrderRec(node.left,dist+1)
            levelOrderRec(node.right,dist+1)
        levelOrderRec(root,1)
        return res

        