class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack=[]
        for c in s:
            if c=="(":
                stack+=["("]
            elif c==")":
                if stack[-1]!="(":
                    temp=stack.pop()[::-1]
                    stack.pop()
                    if stack:
                        if stack[-1]=="(":
                            stack+=[temp]
                        else:
                            stack[-1]=stack[-1]+temp
                    else:
                        stack=[temp]
                else:
                    stack.pop()
            else:
                if stack:
                    if stack[-1]=="(":
                        stack+=[c]
                    else:
                        stack[-1]=stack[-1]+c
                else:
                    stack+=[c]
        
        return ''.join(stack)