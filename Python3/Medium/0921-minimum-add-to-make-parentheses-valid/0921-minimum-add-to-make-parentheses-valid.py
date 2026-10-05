class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack=[]
        for i in range(len(s)):
            el=s[i]
            if el=='(':
                stack.append(el)
            else:
                if not stack:
                    stack.append(el)
                else:
                    prev=stack[-1]
                    if prev=='(':
                        stack.pop()
                    else:
                        stack.append(el)
        
        return len(stack)