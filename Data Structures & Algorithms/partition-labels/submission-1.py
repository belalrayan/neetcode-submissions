class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_index = {c: i for i, c in enumerate(s)}
        res=[]
        end=0
        start=0
        for i,c in enumerate(s):
            end=max(end,last_index[c])
            if end==i:
                res.append(end-start+1)
                start=end+1
        return res        
        