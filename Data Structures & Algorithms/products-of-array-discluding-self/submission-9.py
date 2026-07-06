class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n
        
        # 1. בונים את המכפלות משמאל ישירות בתוך מערך התוצאה
        for i in range(1, n):
            res[i] = res[i - 1] * nums[i - 1]
            
        # 2. עוברים מהסוף להתחלה ומכפילים את מה שמימין
        right_prod = 1
        for i in range(n - 1, -1, -1):
            res[i] *= right_prod
            right_prod *= nums[i]
            
        return res
        