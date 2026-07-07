class Solution:

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        hours_needed=0
        left=1
        right=max(piles)
        best=-1


        while (left<=right):
            mid=int((left+right)/2)
            hours_needed=0
            feasible=True


            for i in range(len(piles)):
                hours,partial_hours=divmod(piles[i],mid)
                hours_needed+=hours
                if partial_hours>0:
                    hours_needed+=1
                if hours_needed>h:
                    left=mid+1
                    feasible=False
                    break
                
            if feasible:
                best=mid        
                right=mid-1
            hourse_needed=0

        return best    




                





        