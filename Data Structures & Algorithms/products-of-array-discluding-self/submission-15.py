class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res=[0]*len(nums)
        if not nums:
            return None

        prod=1
        zeros=0
        
        for num in nums:
            if num==0 :
                zeros+=1
            else:
                prod*=num    

        if zeros>1:
            return res        

        for i,num in enumerate(nums):
            if num==0:
                res=[0]*len(nums)
                res[i]=prod
                return res
            else:
                res[i]=prod//num
        return res            

        