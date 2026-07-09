class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_to_freq={}
        buckets=[[] for i in range(len(nums)+1)]
        res=[]

        for num in nums:
            num_to_freq[num]=num_to_freq.get(num,0)+1

        for num,freq in num_to_freq.items():
            freq=num_to_freq[num]
            buckets[freq].append(num)

        for i in range(len(buckets)-1,0,-1):
            for num in buckets[i]:
                res.append(num)
                if len(res)==k:
                    return res

            
                    

        
        