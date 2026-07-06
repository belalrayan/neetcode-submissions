class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res=[0 for _ in range(len(nums))]
        zeros=0
        index=-1
        prod=1
        for i,num in enumerate(nums):
            if num==0:
                zeros+=1
                if zeros >1:
                    return res
                index = i
            else:
                prod*=num
        for i in range(len(nums)):
            if index==-1:
                res[i]=int(prod/nums[i])
            else:
                if i == index:
                    res[i]=int(prod)
                else:
                    res[i]=0

        return res        
        

        