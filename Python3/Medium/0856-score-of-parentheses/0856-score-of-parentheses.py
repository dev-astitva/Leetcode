class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack=[]
        for i in range(len(s)):
            el=s[i]
            if el=='(':
                stack.append(el)
            else:
                prev=stack[-1]
                if prev=='(':
                    stack[-1]=1
                else:
                    temp=0
                    for j in range(len(stack)-1,-1,-1):
                        c=stack[j]
                        if c!='(':
                            temp+=c
                        else:
                            temp*=2
                            stack=stack[:j]+[temp]  
                            break
  
        return sum(stack)