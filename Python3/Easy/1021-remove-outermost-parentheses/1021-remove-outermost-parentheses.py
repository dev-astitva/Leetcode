class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        if not s:
            return s

        stack=[]
        res=""
        temp=""

        for b in s:
            if stack:
                n=len(stack)
                
                if n==1 and b==")":
                    res=res+temp
                    temp=""
                    stack=[]
                else:
                    temp=temp+b
                    if b=="(":
                        stack+=["("]
                    else:
                        stack.pop() 
            else:
                stack=["("]           
        
        return res