class Solution:
    def jump(self, nums: List[int]) -> int:
        # אם יש איבר אחד בלבד, אנחנו כבר בסוף ולא צריך לקפוץ
        if len(nums) <= 1:
            return 0
            
        jumps = 0
        current_jump_end = 0
        farthest = 0
        
        # רצים עד האיבר הלפני אחרון, כי ברגע שהגענו או עברנו אותו אנחנו כבר יודעים את התשובה
        for i in range(len(nums) - 1):
            # מעדכנים את המקום הכי רחוק שאפשר להגיע אליו מהאינדקס הנוכחי
            farthest = max(farthest, i + nums[i])
            
            # אם הגענו לסוף הטווח של הקפיצה הנוכחית
            if i == current_jump_end:
                jumps += 1 # חייבים לבצע קפיצה נוספת
                current_jump_end = farthest # הטווח הבא שלנו מוגבל ע"י המקום הכי רחוק שהצלחנו לראות
                
                # אופטימיזציה: אם הטווח החדש כבר מגיע לסוף המערך, אפשר לעצור
                if current_jump_end >= len(nums) - 1:
                    break
                    
        return jumps