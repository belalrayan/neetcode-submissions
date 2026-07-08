# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:  
    def isSubtree(self,root,subRoot): 
        self.str1=''
        self.str2=''
        def makestring(root,num):
            if not root:
                if num==1:
                    self.str1+="#"
                    return None
                else:
                    self.str2+="#"
                    return None
            if num==1:
                self.str1+=" @"+str(root.val)+', '            
            else:
                self.str2+=" @"+str(root.val)+', '        
            left=makestring(root.left,num)
            right=makestring(root.right,num)
            return None
        makestring(root,1)
        makestring(subRoot,2)
        if self.str2 in self.str1:
            return  True
        else:
            return False    

