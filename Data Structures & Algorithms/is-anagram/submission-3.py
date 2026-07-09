class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s1,s2= sorted(s),sorted(t)
        return s1==s2

