class MinStack:

    def __init__(self):
        self.mins=[]
        self.elems=[]
        

    def push(self, val: int) -> None:
        self.elems.append(val)
        if len(self.mins) >0:
            self.mins.append(min(self.mins[-1],val))
        else:
            self.mins.append(val)
            

        

    def pop(self) -> None:
        if not self.mins:
            return
        self.elems.pop()
        self.mins.pop()
       
        

        

    def top(self) -> int:
        return self.elems[-1]

    def getMin(self) -> int:
        if not self.mins:
            float('inf')
        return self.mins[-1]
        
