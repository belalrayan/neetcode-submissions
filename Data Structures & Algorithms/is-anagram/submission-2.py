class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        histS,histT= {},{}

        for i in range(len(s)):
            histS[s[i]] =histS.get(s[i],0) +1
            histT[t[i]] = histT.get(t[i],0) + 1
        
        return histS== histT

