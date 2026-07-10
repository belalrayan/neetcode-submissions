class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if len(s)==0:
            return 0
        left=0
        seen={}
        best=1
        for right, c in enumerate(s):
            seen[c]=seen.get(c,0)+1
            max_freq=max(seen.values())
            if(right-left+1)-max_freq>k:
                seen[s[left]]-=1
                if seen[s[left]]==0:
                    del seen[s[left]]
                left+=1

        best=max(best,right-left+1)        

        return best    



            
                

                


