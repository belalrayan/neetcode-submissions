class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n=len(temperatures)
        stack=[]
        res=[0]*n
        for index,num in enumerate(temperatures):
            while stack:
                if num>stack[-1][0]:
                    last_elem=stack.pop()
                    res[last_elem[1]]=index-last_elem[1]
                else:
                    break    
            stack.append((num,index))

        return res

        