class Solution:
    def maxArea(self, heights: List[int]) -> int:
        Area=0
        left=0
        right=len(heights)-1
        while(left<right):
            curr_area=(right-left)*min(heights[right],heights[left])
            Area=max(Area, curr_area)
            if heights[right]>heights[left]:
                left+=1
            else:
                right-=1
        return Area        

        