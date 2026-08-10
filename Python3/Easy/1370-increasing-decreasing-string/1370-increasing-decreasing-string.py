class Solution:
    def sortString(self, s: str) -> str:
        s=list(s)
        res=""
        while s:
            for letter in sorted(set(s)):
                s.remove(letter)
                res+=letter
            for letter in sorted(set(s),reverse=True):
                s.remove(letter)
                res+=letter
        return res