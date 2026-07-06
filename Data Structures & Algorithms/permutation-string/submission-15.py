class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        seen_s1 = {}
        for c in s1:
            seen_s1[c] = seen_s1.get(c, 0) + 1

        # בניית החלון הראשוני עבור len(s1) התווים הראשונים של s2
        seen = {}
        for i in range(len(s1)):
            seen[s2[i]] = seen.get(s2[i], 0) + 1

        # בדיקה אם החלון הראשון הוא כבר פרמוטציה
        if seen == seen_s1:
            return True

        left = 0
        # רצים על שאר התווים של s2, החל מהאינדקס הבא בתור
        for right in range(len(s1), len(s2)):
            # 1. הכנסת התו החדש שנכנס לחלון מימין
            char_in = s2[right]
            seen[char_in] = seen.get(char_in, 0) + 1

            # 2. הוצאת התו הישן שיצא מהחלון משמאל
            char_out = s2[left]
            seen[char_out] -= 1
            if seen[char_out] == 0:
                del seen[char_out]
            
            left += 1    

            # 3. בדיקה האם המצב הנוכחי תואם ל-s1
            if seen == seen_s1:
                return True    

        return False
           