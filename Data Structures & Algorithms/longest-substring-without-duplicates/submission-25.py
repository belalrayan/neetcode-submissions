class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        curr_max=0
        start=0
        seen=set()
        for i,c in enumerate(s):
            if c in seen:
                while s[start]!=c:
                    seen.remove(s[start])
                    start+=1
                start+=1
                
            else:
                seen.add(c)

                curr_max=max(curr_max,i-start+1)
        return  curr_max               



        