class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Treat nums as a linked list: index i points to nums[i]
        # Since there's a duplicate, two indices point to the same value,
        # which creates a cycle. Finding the cycle entry = finding the duplicate.

        slow, fast= nums[0], nums[nums[0]]

        while fast!=slow:
            fast=nums[nums[fast]]
            slow=nums[slow]

        slow=0
        while fast!=slow:
            fast=nums[fast]
            slow=nums[slow]   
        return slow    