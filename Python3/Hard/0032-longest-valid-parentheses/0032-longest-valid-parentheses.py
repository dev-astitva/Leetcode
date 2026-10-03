class Solution:
    def longestValidParentheses(self, s: str) -> int:
        res=0
        stack=[]
        for i in range(len(s)):
            el=s[i]
            if not stack:
                stack+=[el]
            else:
                if el=='(':
                    stack+=[el]
                else:
                    found=False
                    for j in range(len(stack)-1,-1,-1):
                        if stack[j]==True:
                            continue
                        if stack[j]=='(':
                            stack[j]=True
                            found=True
                            break
                    if not found:
                        stack+=[el]

        res=0
        temp=0
        k=0
        while k!=len(stack):
            el=stack[k]
            if el!=True:
                res=max(temp,res)
                temp=0
            else:
                temp+=1
            k+=1
        res=max(temp,res)

        return res*2

        