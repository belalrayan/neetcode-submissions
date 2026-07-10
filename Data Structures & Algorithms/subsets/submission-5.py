class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[]
        path=[]

        def rec(start):
            res.append(path[:])
            for i in range(start,len(nums)):
                path.append(nums[i])
                rec(i+1)
                path.pop()
        rec(0)        
        return res      
        
        
        