class Solution:

    def encode(self, strs: List[str]) -> str:
        final=""
        for s in strs:
            final+= str(len(s)) + "#" +s
        return final    


    def decode(self, s: str) -> List[str]:
        strs=[]
        i=0
        while i < len(s):
            j=i
            while s[j] != "#":
                j+=1

            strs.append(s[j+1:j+1+int(s[i:j])])
            i=j+1+int(s[i:j])    

        return strs    

