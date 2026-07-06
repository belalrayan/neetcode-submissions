class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        seen_s1 = {}
        for c in s1:
            seen_s1[c] = seen_s1.get(c, 0) + 1

        seen = {}
        left = 0
        
        for right, c in enumerate(s2):
            # 1. תמיד מכניסים את התו הנוכחי לחלון
            seen[c] = seen.get(c, 0) + 1
            
            # 2. אם החלון נהיה גדול מדי, מוציאים איבר משמאל ומקדמים את left
            if right - left + 1 > len(s1):
                char_out = s2[left]
                seen[char_out] -= 1
                if seen[char_out] == 0:
                    del seen[char_out]
                left += 1
            
            # 3. בדיקה אם הגענו למצב הנכון
            if seen == seen_s1:
                return True
                
        return False