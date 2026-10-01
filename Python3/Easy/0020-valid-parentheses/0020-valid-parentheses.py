class Solution:
    def isValid(self, s: str) -> bool:
        data={')':'(','}':'{',']':'['}
        stack=[]
        for sym in s:
            if sym in '([{':
                stack.append(sym)
            else:
                if not stack:
                    return False
                else:
                    if stack[-1]!=data[sym]:
                        return False
                    else:
                        stack.pop()
        
        return stack==[]