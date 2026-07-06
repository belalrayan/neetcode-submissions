class Solution:
    def isValid(self, s: str) -> bool:
        opened=[]
        opening=["(","{","["]
        for c in s:
            if c not in opening and len(opened)==0:
                return False
            if c in opening:
                opened.append(c)
            elif c==']' and opened[-1]=="[":
                opened.pop()
            elif c=='}' and opened[-1]=="{":
                opened.pop()
            elif c==')' and opened[-1]=="(":
                opened.pop()
            else:
                return False
        if len(opened)==0:
            return True
        return False

        