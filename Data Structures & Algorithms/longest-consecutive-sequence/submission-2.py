class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set=set(nums)
        longest=0
        
        for num  in num_set:
            length=1
            if num-1 in nums:
                continue
            while num+length in num_set:
                length+=1
            
            longest=max(length,longest)

        return longest   


        