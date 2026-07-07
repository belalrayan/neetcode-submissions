class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Treat nums as a linked list: index i points to nums[i]
        # Since there's a duplicate, two indices point to the same value,
        # which creates a cycle. Finding the cycle entry = finding the duplicate.

        slow, fast = nums[0], nums[nums[0]]

        # Phase 1: find a meeting point inside the cycle
        while slow != fast:
            slow = nums[slow]           # move 1 step
            fast = nums[nums[fast]]     # move 2 steps

        # Phase 2: find the entrance to the cycle (the duplicate number)
        slow = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow