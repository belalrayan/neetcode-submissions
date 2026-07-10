class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res=[]
        comb=[]
        def backtracking(start,goal):
            if goal<0:
                return
            if goal==0:
                res.append(comb[:])

            for i in range(start,len(nums)):
                comb.append(nums[i])
                backtracking(i,goal-nums[i])
                comb.pop()
        backtracking(0,target)
        return res        


        