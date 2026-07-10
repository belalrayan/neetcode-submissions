class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_reachable = 0
        
        for i, jump in enumerate(nums):
            # אם הגענו לאינדקס שאי אפשר להגיע אליו מהשלבים הקודמים
            if i > max_reachable:
                return False
            
            # עדכון המרחק המקסימלי שאפשר להגיע אליו
            max_reachable = max(max_reachable, i + jump)
            
            # אופטימיזציה: אם כבר הגענו או עברנו את האינדקס האחרון
            if max_reachable >= len(nums) - 1:
                return True
                
        return True