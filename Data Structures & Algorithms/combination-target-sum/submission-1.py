class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res=[]
        sub=[]

        def backtrack(start,remain):
            if remain==0:
                res.append(sub[:])

            if remain<0:
                return
            for i in range(start,len(nums)):
                sub.append(nums[i])
                backtrack(i,remain-nums[i])
                sub.pop()
        backtrack(0,target)
        return res            
                    

        