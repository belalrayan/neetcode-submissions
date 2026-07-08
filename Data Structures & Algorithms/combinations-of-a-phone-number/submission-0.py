class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
            
        # מיפוי הספרות לאותיות המתאימות
        digit_to_letters = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }
        
        res = []
        
        def backtrack(index, current_str):
            # תנאי עצירה: בנינו שילוב באורך מלא
            if len(current_str) == len(digits):
                res.append(current_str)
                return
                
            # לוקחים את הספרה הנוכחית ואת האותיות שלה
            current_digit = digits[index]
            letters = digit_to_letters[current_digit]
            
            # עוברים על כל אות אפשרית ומקדמים את האינדקס ברקורסיה
            for letter in letters:
                backtrack(index + 1, current_str + letter)
                
        backtrack(0, "")
        return res