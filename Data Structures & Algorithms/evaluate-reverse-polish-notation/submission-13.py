class Solution:
    def operation(self,a:int,b:int,c:str) -> int:
        if c=="+":
            return a+int(b)
        if c=="*":
            return a*int(b)
        if c=="-":
            return a-int(b)
        if c=="/":
            return int(a/int(b))

    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            if t in ("+", "-", "*", "/"):
                b = stack.pop()
                a = stack.pop()
                stack.append(self.operation(a, b, t))
            else:
                stack.append(int(t))
        return stack[0]
            