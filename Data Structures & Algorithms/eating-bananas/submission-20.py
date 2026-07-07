class Solution:

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left=1
        right=max(piles)
        best=right
        while(left<=right):
            mid=(left+right)//2
            hours_needed=0
            
            feasible=True
            for i in range(len(piles)):
                hours_needed+=piles[i]//mid
                if piles[i]%mid >0:
                    hours_needed+=1
                if hours_needed>h:
                    feasible=False
                    left=mid+1
                    break
                
            if feasible:
                best=min(mid,best)
                right=mid-1

        return best                

                



                





        