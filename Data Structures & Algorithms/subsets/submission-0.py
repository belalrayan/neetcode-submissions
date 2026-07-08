class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []

        def backtrack(start):
            res.append(path[:])          # every state of path is a valid subset
            for i in range(start, len(nums)):
                path.append(nums[i])     # choose nums[i]
                backtrack(i + 1)         # explore
                path.pop()               # un-choose (backtrack)

        backtrack(0)
        return res