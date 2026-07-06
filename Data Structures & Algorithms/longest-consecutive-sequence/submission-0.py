class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set=set(nums)
        longest=0
        
        for num  in nums:
            length=1
            if num-1 in nums:
                continue
            while num+length in nums:
                length+=1
            
            longest=max(length,longest)

        return longest   


        