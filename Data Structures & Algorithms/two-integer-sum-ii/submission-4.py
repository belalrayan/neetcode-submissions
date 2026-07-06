class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left,right=1,len(numbers)
        while(left<right):
            if numbers[right-1]+numbers[left-1]==target:
                return [left,right] 
            elif numbers[right-1]+numbers[left-1]>target:
                right-=1
            else:
                left+=1    
        