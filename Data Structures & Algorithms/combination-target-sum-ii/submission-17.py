class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        sub=[]
        candidates.sort()
        def backtrack(start,goal):
            if goal<0:
                return
            if goal==0:
                res.append(sub[:])   
            for  i in range(start,len(candidates)):
                if i>start and candidates[i]==candidates[i-1]:
                    continue
                sub.append(candidates[i])
                backtrack(i+1,goal-candidates[i])
                sub.pop()
        backtrack(0,target)
        return res         
        