class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        prev1, prev2 =0,0
        min_c=0
        for i in range(2,len(cost)+1):
            min_c=min(prev1+cost[i-2],prev2+cost[i-1])
            prev1, prev2=prev2, min_c
        return min_c    


        