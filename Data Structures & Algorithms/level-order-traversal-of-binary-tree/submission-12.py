# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res=[]
        def dfs(node,dist):
            if not node:
                return
            if len(res)<=dist:
                res.append([])

            res[dist].append(node.val)
            dfs(node.left,dist+1)
            dfs(node.right,dist+1)    
        dfs(root,0)
        return res    
        
        