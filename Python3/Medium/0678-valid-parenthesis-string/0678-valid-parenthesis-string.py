class Solution:
    def checkValidString(self, s: str) -> bool:
        stack=[]
        for i in range(len(s)):
            el=s[i]
            if el in '(*':
                stack.append(el)
            else:
                if not stack:
                    return False
                else:
                    found=False
                    for j in range(len(stack)-1,-1,-1):
                        if stack[j]=='(':
                            found=True
                            stack[j]=True
                            break
                    if not found:
                        found=False
                        for j in range(len(stack)-1,-1,-1):
                            if stack[j]=='*':
                                found=True
                                stack[j]=True
                                break
                        if not found:
                            return False
     
        temp=[]
        for k in range(len(stack)):
            el=stack[k]
            if el=='(':
                temp.append((el,k))

            elif el=='*':
                if not temp:
                    continue
                else:
                    elem,idx=temp.pop()
                    stack[idx]=True
                    stack[k]=True

        # print(stack)
        return not ('(' in stack or ')' in stack)