class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1 = sorted(s1)
        left = 0
        
        # רצים על האינדקסים האמיתיים של s2, החל מהאינדקס שיכול לסגור את החלון הראשון
        for right in range(len(s1) - 1, len(s2)): 
            # כעת left ו-right הם אינדקסים אמיתיים ומדויקים בתוך s2
            sub = sorted(s2[left : right + 1])
            
            if sub == s1:
                return True
                
            left += 1
            
        return False