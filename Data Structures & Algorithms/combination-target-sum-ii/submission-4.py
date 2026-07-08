class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        sub,res=[],[]
        candidates.sort()


        def backtrack(start,target):
            if target==0:
                res.append(sub[:])

            if target<0:
                return

            for i in range(start,len(candidates)):
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                sub.append(candidates[i])
                backtrack(i+1,target-candidates[i])
                sub.pop()
        backtrack(0,target)
        return res            