class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res=[]
        n=len(nums)
        for i in range(len(nums)-2):
            if i>0 and nums[i]==nums[i-1]:
                continue
            target=nums[i]
            start=i+1
            end=len(nums)-1
            while start<end:
                if nums[start]+nums[end]==-nums[i]:
                    res.append([nums[i],nums[start],nums[end]])
                    start+=1
                    end-=1
                    while start<end and nums[start]==nums[start-1]:   # ADD THIS
                        start+=1
                    while start<end and nums[end]==nums[end+1]:        # ADD THIS
                        end-=1
                elif nums[start]+nums[end]>-nums[i]:
                    end-=1
                else:
                    start+=1

        return res                


            
            
        

        