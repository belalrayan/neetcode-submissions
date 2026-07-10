class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res=[]
        stri=''
        def backtrack(opened,closed):
            nonlocal stri
            if len(stri)==2*n:
                res.append(stri[:])
                return
            if opened<n:
                opened+=1
                stri+=('(')
                backtrack(opened,closed)
                stri=stri[:-1]

                opened-=1

            if opened>closed:
                closed+=1
                stri+=(')')
                backtrack(opened,closed)
                stri=stri[:-1]
                closed-=1
        backtrack(0,0)
        return res        









        