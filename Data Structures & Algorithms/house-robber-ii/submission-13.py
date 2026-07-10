def rob_linear(profit):
    if not profit:
                return 0
    if len(profit)==1:
        return profit[0]    
    prev1,prev2= profit[0],max(profit[0],profit[1])
    for i in range(2,len(profit)):
        curr=max(profit[i]+prev1,prev2)
        prev1,prev2=prev2,curr
    return prev2    
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len (nums)==1:
            return nums[0]    
        
        return max(rob_linear(nums[1:]),rob_linear(nums[:-1]))        

        