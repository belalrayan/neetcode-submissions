# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSubtree(self, root, subRoot):
        def serialize(node):
            parts = []
            def helper(n):
                if not n:
                    parts.append("#")
                    return
                helper(n.left)
                helper(n.right)
                parts.append("^" + str(n.val))
            helper(node)
            return " ".join(parts)

        return serialize(subRoot) in serialize(root)