class Solution:
    def minInsertions(self, s: str) -> int:
        s=s.replace('))','#')
        stack=[]
        res=0
        for el in s:
            if not stack:
                if el==')':
                    res+=2
                elif el=='#':
                    res+=1
                else:
                    stack+=['(']
            else:
                if el=='#':
                    prev=stack[-1]
                    if prev=='(':
                        stack.pop()
                elif el==')':
                    stack.pop()
                    res+=1
                else:
                    stack+=['(']

        res+=len(stack)*2
        return res