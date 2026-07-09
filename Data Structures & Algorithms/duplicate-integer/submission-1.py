class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if not nums:
            return False
        hist={}
        for num in nums:
            if num in hist:
                return True
            hist[num]=1
        return False              