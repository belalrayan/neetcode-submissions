class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        current_permutation = []
        used = [False] * len(nums)
        
        def backtrack():
            if len(current_permutation) == len(nums):
                res.append(current_permutation[:])
                return
            
            for i in range(len(nums)):
                if not used[i]:
                    used[i] = True
                    current_permutation.append(nums[i])
                    
                    backtrack()
                    
                    current_permutation.pop()
                    used[i] = False
                    
        backtrack()
        return res