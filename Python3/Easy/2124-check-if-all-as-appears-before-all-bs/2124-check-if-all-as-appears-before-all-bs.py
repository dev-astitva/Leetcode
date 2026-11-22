class Solution:
    def checkString(self, s: str) -> bool:
        b_appeared=False
        for c in s:
            if c=="b":
                b_appeared=True
            else:
                if b_appeared:
                    return False
        return True