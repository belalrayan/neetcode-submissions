# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        self.str1=''
        self.str2=''
        def stri(curr,num):
            if not curr:
                if num==1:
                    self.str1+='#'
                else:
                    self.str2+='#'    
                return
            left=stri(curr.left,num)
            right=stri(curr.right,num)
            
            if num==1:
                self.str1+=str(curr.val)
            else:
                self.str2+=str(curr.val)    
            return


        stri(p,1)
        stri(q,2)
        return self.str1==self.str2    

        