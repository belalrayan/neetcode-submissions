class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums) - 2):              # CHANGED: iterate by index, stop 2 before end
            if i > 0 and nums[i] == nums[i - 1]:     # ADDED: skip duplicate targets
                continue
            target = nums[i]
            left = i + 1                             # CHANGED: start left after target's index
            right = len(nums) - 1
            while left < right:
                if nums[left] + nums[right] == -target:
                    res.append([target, nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while right > i and nums[right] == nums[right + 1]:   # CHANGED: compare to previous accepted value, bound by i
                        right -= 1
                    while left < right and nums[left] == nums[left - 1]:  # CHANGED: compare to previous accepted value
                        left += 1
                elif nums[left] + nums[right] > -target:
                    right -= 1
                else:
                    left += 1
        return res
        