class TimeMap:

    def __init__(self):
        self.dict={}

        

    def set(self, key: str, value: str, timestamp: int) -> None:
        pair=self.dict.get(key,[])
        pair.append((timestamp,value))
        self.dict[key]=pair

        

    def get(self, key: str, timestamp: int) -> str:
        key_pairs=self.dict.get(key,[])
        left=0
        right=len(key_pairs)-1
        while(left<=right):
            mid=(left+right)//2
            if(key_pairs[mid][0]==timestamp):
                return key_pairs[mid][1]
            if(key_pairs[mid][0] <timestamp):
                left=mid+1
            else:
                right=mid-1
        if right<0:
            return ""
        return key_pairs[right][1]         
            

        
