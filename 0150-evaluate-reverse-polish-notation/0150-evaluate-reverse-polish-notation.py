class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        operations=["*","+","-","/"]
        for i in tokens:
            if i in operations:
                a=stack.pop()
                b=stack.pop()
                stack.append(str(int(eval(b+i+a))))
            else:
                stack.append(i)
        return int(stack[-1])