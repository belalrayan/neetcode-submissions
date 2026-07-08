class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res=[]
        curr_perm=[]
        used=[False]*len(nums)

        def backtrack():
            if len(curr_perm)==len(nums):
                res.append(curr_perm[:])
                return

            for i in range(len(nums)):
                if not used[i]:
                    used[i]=True
                    curr_perm.append(nums[i])
                    backtrack()
                    curr_perm.pop()
                    used[i]=False
        backtrack()
        return res            
